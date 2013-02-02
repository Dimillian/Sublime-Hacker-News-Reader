#V1.3

import sublime
import sublime_plugin
import threading
from libs.hnapi import *

hackernews = "http://news.ycombinator.com/rss"
hnAPi = HackerNewsAPI()

class HackerNewsReader(sublime_plugin.WindowCommand):
	def run(self):
		sublime.status_message('Loading Hacker News Feed')

		thread = HNRSSLoad(self.onThreadResult)
		thread.start();

	def onThreadResult(self, data):
		self.hnData = data
		sublime.set_timeout(self.displayItems, 0)

	def displayItems(self):
		self.feed_text = []
		for item in self.hnData:
			first_line = '%s. %s' % (item.number, item.title.decode('utf8'))
			second_line = 'vote: %s comments: %s (%s)' % (item.score, item.commentCount, item.domain)
			self.feed_text.append([first_line, second_line])

		self.window.show_quick_panel(self.feed_text, self.onItemSelection)

	def onItemSelection(self, index):
		if (index != -1):
			self.selected_item = index
			menu_text = []
			menu_text.append('Read the article')
			menu_text.append('Open comments on Hacker News')
			self.window.show_quick_panel(menu_text, self.onMenuChoiceSelection)

	def onMenuChoiceSelection(self, index):
		if (index != -1):
			if (index == 1):	
				url = self.hnData[self.selected_item].commentsURL
			else:
				url = self.hnData[self.selected_item].URL
			import webbrowser
			webbrowser.open(url)

class HNRSSLoad(threading.Thread):
	def __init__(self, callback):
		self.result = None
		threading.Thread.__init__(self)
		self.callback = callback
	def run(self):
		self.result = hnAPi.getTopStories()
		self.callback(self.result)
		return