#!/usr/env python

import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
  def get(self):
    self.write("hello, world!")

class StoryHandler(tornado.web.RequestHandler):
  def get(self, story_id):
    self.write("You requested the story" + story_id)

class RestHandler(tonado.web.RequestHandler):
  pass

class Hello_worldHandler(tornado.web.RequestHandler):
  def get(self):
    self.write("get")
  def put(self):
    self.write("put")
  def post(self):
    self.write("post")
  def delete(self):
    self.write("delete");
  def w(self):
    self.write("iamw");

application = tornado.web.Application([
  (r"/", MainHandler),
  (r"/story/([0-9]+)", StoryHandler),
  (r"/hello_world", Hello_worldHandler),

])

if __name__ == "__main__":
  application.listen(8888)
  tornado.ioloop.IOLoop.instance().start()
