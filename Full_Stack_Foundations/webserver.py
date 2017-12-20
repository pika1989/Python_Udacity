import cgi
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

from database_setup import Base, Restaurant, MenuItem
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

class webserverHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            if self.path.endswith('/restaurants/new'):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                
                output = ''
                output += '<html><body>'
                output += '<h1> Make a New Restaurant</h1>'
                output += ''.join(('<form method="POST" enctype="multipart/form-data" action="/restaurants/new">',
                                   '<input name="newRestaurantName" type="text" placeholder="New Restaurant Name">',
                                   '<input type="submit" value="Create">',
                                   '</form>'))
                output += '</body></html>'

                self.wfile.write(output)
                return

            if self.path.endswith('/edit'):
               restaurant_id_path = self.path.split('/')[2]
               restaurant_for_edit = session.query(Restaurant).filter_by(id = restaurant_id_path).one()

               if restaurant_for_edit != []:
                   self.send_response(200)
                   self.send_header('Content-type', 'text/html')
                   self.end_headers()

                   output = ''
                   output += '<html><body>'
                   output += '<h1>%s</h1>' % restaurant_for_edit.name
                   output += ''.join(('<form method="POST" enctype="multipart/form-data" action="/restaurants/%s/edit">' % restaurant_id_path,
                                      '<input name="newRestaurantName" type="text" placeholder="%s">' % restaurant_for_edit.name,
                                      '<input type="submit" value="Rename">',      
                                      '</form>'))
                   output += '</body></html>'
                   self.wfile.write(output)
                   return

            if self.path.endswith('/delete'):
               restaurant_id_path = self.path.split('/')[2]
               restaurant_for_delete = session.query(Restaurant).filter_by(id = restaurant_id_path).one()

               if restaurant_for_delete != []:
                   self.send_response(200)
                   self.send_header('Content-type', 'text/html')
                   self.end_headers()

                   output = ''
                   output += '<html><body>'
                   output += '<h1>Are you sure you want to delete %s?</h1>' % restaurant_for_delete.name
                   output += ''.join(('<form method="POST" enctype="multipart/form-data" action="/restaurants/%s/delete">' % restaurant_id_path,
                                      '<input type="submit" value="Delete">',      
                                      '</form>'))
                   output += '</body></html>'
                   self.wfile.write(output)
                   return

            if self.path.endswith('/restaurants'):
                restaurants = session.query(Restaurant).all()

                output = ''
                output += '<a href = "/restaurants/new"> Make a New Restaurant Here </a></br></br>'

                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()

                output += '<html><body>'
                for restaurant in restaurants:
                    output += '%s </br>' % restaurant.name
                    output += '<a href="/restaurants/%s/edit">Edit</a></br>' % restaurant.id
                    output += '<a href="/restaurants/%s/delete">Delete</a></br></br>' % restaurant.id
                output += '</body></html>'

                self.wfile.write(output)
                return
        except IOError:
            self.send_error(404, 'File Not Found %s' % self.path)

    def do_POST(self):
        try:
             if self.path.endswith('/delete'):
                 ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
                 if ctype == 'multipart/form-data':
                     restaurant_id_path = self.path.split('/')[2]
                     restaurant_for_delete = session.query(Restaurant).filter_by(id = restaurant_id_path).one()
                     
                     if restaurant_for_delete != []:
                         session.delete(restaurant_for_delete)
                         session.commit()
                         self.send_response(301)                                    
                         
                         self.send_header('Content-type', 'text/html')              
                         self.send_header('Location', '/restaurants')               
                         self.end_headers() 
                         

             if self.path.endswith('/edit'):
                 ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
                 if ctype == 'multipart/form-data':
                     fields = cgi.parse_multipart(self.rfile, pdict)
                     messagecontent = fields.get('newRestaurantName')

                     restaurant_id_path = self.path.split('/')[2]
                     restaurant_for_edit = session.query(Restaurant).filter_by(id = restaurant_id_path).one()

                     if restaurant_for_edit != []:
                         restaurant_for_edit.name = messagecontent[0]

                         session.add(restaurant_for_edit)
                         session.commit()
                         self.send_response(301)                                    
                         
                         self.send_header('Content-type', 'text/html')              
                         self.send_header('Location', '/restaurants')               
                         self.end_headers() 

             if self.path.endswith('/restaurants/new'):
                 ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
                 if ctype == 'multipart/form-data':
                     fields = cgi.parse_multipart(self.rfile, pdict)
                     messagecontent = fields.get('newRestaurantName')

                     newRestaurant = Restaurant(name=messagecontent[0])
                     print newRestaurant.name
                     session.add(newRestaurant)
                     session.commit()

                     self.send_response(301)
                     self.send_header('Content-type', 'text/html')
                     self.send_header('Location', '/restaurants')
                     self.end_headers()
        except Exception as err:
            print err
            pass


def main():
    try:
        port = 8080
        server = HTTPServer(('', port), webserverHandler)
        print 'Web server running on port %s' % port
        
        server.serve_forever()
    except KeyboardInterrupt:
        print '^C entered, stopping web server...'
        server.socket.close()


if __name__ == '__main__':
    main()
