from Plotter import graph
import cherrypy 

class Root: 
    @cherrypy.expose 
    def index(self):
        graph()
        return "<img src='/images/foo.png'>"
    index.exposed = True

cherrypy.quickstart(Root(), '/', 'server.conf') 
