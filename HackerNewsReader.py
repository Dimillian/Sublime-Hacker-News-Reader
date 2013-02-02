import sublime
import sublime_plugin
import threading
import requests as rq
from libs.feedparser import parse

hackernews = "http://news.ycombinator.com/rss"

class HackerNewsReader(sublime_plugin.WindowCommand):
	def run(self):
		sublime.status_message('Loading Hacker News Feed')
		thread = HNRSSLoad(5, self.onThreadResult)
		thread.start();

	def onThreadResult(self, data):
		#Check data integrity before main thread
		self.hnData = data
		sublime.set_timeout(self.displayItems, 0)

	def displayItems(self):
		self.feed = parse(self.hnData)
		self.feed_text = []
		for item in self.feed['entries']:
			self.feed_text.append([item['title'], item['link']])

		self.window.show_quick_panel(self.feed_text, self.onItemSelection)

	def onItemSelection(self, index):
		#url = presentation[0]
		url = self.feed['entries'][index]['link']
		import webbrowser
		webbrowser.open(url)

class HNRSSLoad(threading.Thread):
	def __init__(self, timeout, callback):
		self.timeout = timeout
		self.result = None
		threading.Thread.__init__(self)
		self.callback = callback
	def run(self):
		try:
			self.result = rq.get(hackernews).text
			self.callback(self.result)
			return
		except (rq.exceptions.ConnectionError) as (e):
			err = 'No internet connection'
		except (rq.exceptions.HTTPError) as (e):
			err = 'Bad HTTP Response'
		sublime.error_message(err)
		self.result = False