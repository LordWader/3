from Plotter import graph
import cherrypy 

class Root: 
    @cherrypy.expose 
    def index(self):
        graph()
        return """
        <!DOCTYPE HTML>
        <html>
         <head>
          <meta charset="utf-8">
          <meta http-equiv="Refresh" content="5" />
          <title>Bar Chart</title>
         </head>
         <body> 
          <p><img src='/foo.png'></p>
        </body>
        </html>
        """
    index.exposed = True

cherrypy.quickstart(Root(), '/', 'server.conf')
