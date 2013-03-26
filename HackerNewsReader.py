#V1.5

import sublime
import sublime_plugin
import threading
from libs.hnapi import *

always_online_url = "http://google.com"
hn_url = "https://news.ycombinator.com/"
timeout = 2

hnAPi = HackerNewsAPI()

class HackerNewsReader(sublime_plugin.WindowCommand):
	def run(self):
		sublime.status_message('Loading Hacker News Feed...')
		statusThread = CheckStatus(self.onInternetThreadResult, always_online_url, hn_url, timeout)
		statusThread.start()
		newsThread = HNRSSNewsLoad(self.onNewsThreadResult)
		newsThread.start()

	def onNewsThreadResult(self, data):
		self.hnData = data
		sublime.set_timeout(self.displayItems, 0)

	def displayItems(self):
		self.feed_text = []
		for item in self.hnData:
			first_line = '%s. %s' % (item.number, item.title.decode('utf8'))
			second_line = '%s by %s | %s comments (%s)' % (item.score, item.submitter, item.commentCount, item.domain)
			self.feed_text.append([first_line, second_line])

		self.window.show_quick_panel(self.feed_text, self.onItemSelection)

	def onItemSelection(self, index):
		if (index != -1):
			self.selected_item_index = index
			item = self.hnData[index]
			menu_text = []
			menu_text.append('Read the article in browser')
			menu_text.append('Open comments on Hacker News')
			menu_text.append('About %s' % item.submitter)
			self.window.show_quick_panel(menu_text, self.onMenuChoiceSelection)

	def onMenuChoiceSelection(self, index):
		if (index != -1):
			if (index == 1):	
				self.openURL(self.hnData[self.selected_item_index].commentsURL)
			elif (index == 0):
				self.openURL(self.hnData[self.selected_item_index].URL)
			else:
				item = self.hnData[self.selected_item_index]
				statusThread = CheckStatus(self.onInternetThreadResult, always_online_url, hn_url, timeout)
				statusThread.start()
				userThread = HNRSSUserLoad(self.onUserThreadResult, item.submitter)
				userThread.start()
				url = None

	def onUserThreadResult(self, data):
		self.userData = data
		sublime.set_timeout(self.displayUser, 0)

	def displayUser(self):
		menu_text = []
		first_line = self.userData.name
		second_line = '%s karma | %s' % (self.userData.karma, self.userData.userPageURL)
		menu_text.append([first_line, second_line])
		self.window.show_quick_panel(menu_text, self.onUserMenuChoiceSelection)

	def onUserMenuChoiceSelection(self, index):
		if (index != 1):
			self.openURL(self.userData.userPageURL)

	def openURL(self, url):
		import webbrowser
		webbrowser.open(url)

	def onInternetThreadResult(self, status):
		if (not status):
			sublime.set_timeout(self.displayError, 0)

	def displayError(self):
		sublime.status_message('Your Internet connection seems to be down, could you please check it for me?')
		

class HNRSSNewsLoad(threading.Thread):
	def __init__(self, callback):
		self.result = None
		threading.Thread.__init__(self)
		self.callback = callback
	def run(self):
		self.result = hnAPi.getTopStories()
		self.callback(self.result)
		return

class HNRSSUserLoad(threading.Thread):
	def __init__(self, callback, username):
		self.username = username
		self.result = None
		threading.Thread.__init__(self)
		self.callback = callback
	def run(self):
		user = HackerNewsUser(self.username)
		self.result = user
		self.callback(self.result)
		return

class CheckStatus(threading.Thread):
	def __init__(self, callback, check_url, service_url, timeout):
		self.timeout = timeout
		self.check_url = check_url
		self.service_url = service_url
		threading.Thread.__init__(self)
		self.callback = callback
	def run(self):
		try:
			urllib2.urlopen(self.check_url, timeout=self.timeout)
			self.callback(True)
		except:
			self.callback(False)
		return