import tornado.ioloop
from handler.base import MainHandler
from handler.city import CityHandler
from handler.station import StationHandler
from handler.aqi import AqiHandler
from db.base import conn
from db.city import create_table_city
from db.station import create_table_station
from db.aqi import create_table_city_aqi


def make_app():
    return tornado.web.Application([
        (r'/', MainHandler, dict(conn=conn)),
        (r'/city', CityHandler, dict(conn=conn)),
        (r'/station', StationHandler, dict(conn=conn)),
        (r'/aqi', AqiHandler, dict(conn=conn)),
    ])


if __name__ == '__main__':
    create_table_city(conn)
    create_table_station(conn)
    create_table_city_aqi(conn)
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
