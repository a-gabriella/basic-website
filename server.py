#data from https://www.kaggle.com/jackywang529/michelin-restaurants?select=three-stars-michelin-restaurants.csv

from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)


current_id_res = 10
restaurants = [
    {'1': {'id': 1, 'title': 'Amador', 'year': '2019', 'latitude': '48.25406', 'longitude': '16.35915', 'city': 'Wien', 'region': 'Austria',
                'zipCode': '1190', 'cuisine': 'Creative', 'price': '$$$$$', "wine": ["Margaux", "Screaming Eagle", "Château Latour", "Ridge"], 'description': 'Few people eat here. Is the food a good value? Few know the answer. This is the 4th sentence.',
                'url': 'https://axwwgrkdco.cloudimg.io/v7/mtp-cf-images.s3-eu-west-1.amazonaws.com/images/max/9d89fb7e-a8ff-4bb3-a8e0-cdf29003e7dc.jpg?width=1000', 'link': 'http://127.0.0.1:5000/view/1'},
     '2': {'id': 2, 'title': 'Manresa', 'year': '2019', 'latitude': '37.22761', 'longitude': '-121.98071', 'city': 'South San Francisco',
                 'region': 'California', 'zipCode': '95030', 'cuisine': 'Contemporary', 'price': '$$$$', "wine": ["Margaux", "Screaming Eagle", "Château Latour", "Ridge"], 'description': 'Few people eat here. Is the food a good value? Few know the answer. This is the 4th sentence.',
                 'url': 'https://s.hdnux.com/photos/60/22/02/15351870/7/1236x0.jpg', 'link': 'http://127.0.0.1:5000/view/2'},
     '3': {'id': 3, 'title': 'Benu', 'year': '2019', 'latitude': '37.78521', 'longitude': '-122.39876', 'city': 'San Francisco',
              'region': 'California', 'zipCode': '94105', 'link': 'http://127.0.0.1:5000/view/3', 'cuisine': 'Asian', 'price': '$$$$', "wine": ["Margaux", "Screaming Eagle", "Château Latour", "Ridge"], 'description': 'Few people eat here. Is the food a good value? Few know the answer. This is the 4th sentence.',
              'url': 'data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAoHCBUVEhgVFRUYGRgYGhgYGhoaGBoaGBgYGBgZGRgYGRgcIS4lHB4rHxgYJjgmKy8xNzU1GiQ7QDs0Py40NTEBDAwMEA8QHxISHzQrJSs0NDQ0NjQ0NDQ0NDQ1NDQ0NDY0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NjQ0NDQ0NP/AABEIALABHgMBIgACEQEDEQH/xAAcAAABBQEBAQAAAAAAAAAAAAADAAIEBQYBBwj/xABAEAACAQIEAwYDBAgGAgMBAAABAgADEQQSITEFQVEGImFxgZETMqFCUrHBBxRDYoLR4fAVI1NykvEzojSy0hb/xAAaAQEAAwEBAQAAAAAAAAAAAAAAAQIDBAUG/8QALBEAAgIBAwMCBQQDAAAAAAAAAAECEQMSITEEQVETFCJhgZGxBUJxoSMyUv/aAAwDAQACEQMRAD8A8fyxWj8sWWCRlogI/LEBAGETloS04VgDCJy0JaK0AHaK0JadyQSByxZYXJFkgAssWWFtOFYAPLOWhcsWWACtFaEKzmWADnLR5E5aCBsU7OQBRRRQQKKKKAKKKKAKKKKAKKKKAKKKKAKKKKAT8kWSSckWSARsk78OSckctMQCGUnTTkr4XhOmgYBC+HO5JMFKFTAu3yox8lJ/KCSuyGd+HLul2fxLfLRf/iR+MlU+yOLb9iw8yP5xZJmjTi+HNcvYfFn7CjzaGTsFiba5P+R/lFkGK+HOtTm3H6PsQd2Qep/lOj9Htf76fWLBhMsRSbo/o9r/AH0+sa/6P64BJenYAknXQDcyLJMMUnCk2VHsLWdA6VKTq2oKsbH6Tj9g8UOSH+L+kWDF5I0pNfU7FYsfYB8mEg1uyWLX9gx8iD+cWDNlY2XFbgWJX5qDj+G/4SvqYR1+ZHHmrD8RJsUR5y0cYoFDbTs6IoFDTFOxQRRyKK0UECiiigCiiigCiiigGl+B0BhaOCZjZUcnwBP4T1DC9ncOn2Mx6sb/AE2lpRoKuiqB5ACAeY4XsrXf9my+LELLbD9g3Pz1FXwAJM36rHhYBkcN2EoD53dvUAfSWdDsphV/ZBv9xLfjL4LHBYBAo8Lop8tJB5KJKWiBsAPIQXFOIJh6RqvfKCB3QCdTbQEjz9I/h+Op10z0nDrtpuD0YbqfAyNromnVhcsWWGyyj4z2mw+GW7OD1sb9drXzG45ba3IkkchKnGKS4g0HJVgFIJHcOYXAvfQ+eksss8m452mTEVVqLSe62G6oGCkkXHfJgMRx1VLZkqNmF7DFVsoe+oIVgMu+3hM4zdtP6G0oKk4/U9VOPoh2Q1UDJ8wLAFdAdb+BExWA7RU8MHL1lqpny5EdWc3J/wAxBe2XqL+1tcWOM0r3OFpX6kO1/Msxkul2gofawNIj93u2/wDUyHu0/BMVScfJ6FS7aYRtjU2v/wCJzyvuLj6zg7YYR1Ib4gVgRc0nIKkWvdb/AFmIw3EqdSoL5xTzCyO2YgH5xcBRbYC+vjIvF6K0cQ6qXQZrpclGCk929uY2PlKPM9VUa+3pJ2XXCeMDCd4OWpNmypbV1W1m/cJB3PTaaj/+uwzUs6FmbT/LykPc+emmuoMwFfDOKqVP1hXNwRkqo9+ZFlvlHW4t5yXj1IZKhYBnvdVRVVQrDTuqLknnzt4aZ+qoKkb+g8j1yW35PUaZDqGXUEAj1kGpxKmuIGHJIdlzDTunfu3+9YXnnGIxTJUZ6bsilg4sct7WsSoJHLxhsRxHENUXEPTzFCrfEVSuaxBUFhddttpdZ9S2Rh7ZJu2emMkC+HU7qD6CZbG9t0qUstJWSo1wQwuVGxII0v0Osu+yjO2ETOSbEqCd8o2uefPWba03pMpYZRhrfF0Or8Jov81JD5qJV4jslhG/YqL/AHdPwmoZIxklqMbMLif0f4Y/Izp63/GVOJ/R4w+SsD4Mv5iemmnGFIoWeP4nsVi02RWH7ra+xlPieFV0+ek4/hJHuNJ7qacG9IHcQLPACIp7djOBYep89JD45Rf3lDjOweHb5CyHwNx7GCTy+ctNjjewdddUZHHT5TM9i+E16fz0nXxtce40ixRXxRxWcIkkUciitFBB9KAR6rEoj1EASrHhZ1RHAQBAToEo+PdpUwrBWpu5K5u7lAAJtuxBO3IG2l95DwHbvCu4R89NjtnAym+3eBIHrK6ldWW0Sq6LvjXDhicO9Em2caH7rA3U25i4HpeeQUcc+AxZszh1DpUAPdz2YLcD51Bs2tpqO0/bpiWo4QEWurVe7e9yCEGot+97TCU8KXLZmYljmYkk3bXVidzqdfEyk5RTvwaR1JV5LXH9pMViLg1Hy6b5L+gUBeV7hbjrK/DcOJ3trbTcvqNNNzcg28po+G8PFdhSop8qjMT8qm1jc63ubkdfCbvgnAaOH+yGqHeowF/IdBOd5JSL1GKMRgeyr5MxTKSRoeQ8vaSanZdrHb2npDYe87SwovrMvTld2R6nyPGsX2dOtk3PKVVfgjrpqATqNvee5VaSXIy+ttZW4zgyMCdDfraWU5x43Fp8o8aXCunpG18YX/8AJcsNLkknbxnomN7NMb5Bf8JkeJ8GZG7ykekLJFv4tjVW+CFwykA+ZeQvvy9Zc8UqLUKFAQQoBB2vc3C87a85nhQZDcH1ljhcYGsrWuNOl/G/XWUyJt6ludMJ2tLHcSogrlBN8uoa90e/eA29tdzC8DwzZWUldAWOvJR9TrtOs7A5hqddTruNd/ODpuQtibWN7W1uRqb+g/u8jVcaEZOEm0SKop50y/KfnupAQnSygMS2XQ3vr066js52kCjJWyqgvZwLAFmLWYDQDU7DQDpe2TqUiGKsLNp9dRGG9gOl/wC7+kQyOLtFJx1xpnqz8SoBM/xUy/eDqR7gwtGorqHRgytqCDcGeZ0cMPiB3KoWFtQLlxZbFV+W9tz585fcIw71nNGo10Qtamj5VUHUPUKDv95rizDVSDbSdcM7lKqOefTqMbTNgUjCklFI34c6TkIxSMKSYacaUgEI04xkk0pBulgSdAIBBqKALnQRlSj1G+vI+4lpTwakhnAYjUAi6i+xtzP4SwZFZMpVfQWnL7qLk0i9UjB4/s3hqt89JQeq90+4max/YIamlU/hcfmJ6hisGALqLSC1KbxkpK0Vs8W4h2dxFL56Zt95e8PpKk0zPeXpSqxvAMPVN3pi/UaE+dpYWbBSIRTKNMUYVcU0kguljgJUpjDCLjjAJXEOG066ZKqBhyOzKeqnkZ49icKhqvTWxCVHUNbvMFawY8uWlupnovaHjpo4dmvZmBVRrckixsRsRe9/Dxnm+AQoM29/pOfNX1OjFJpEulgEBCjdvc+Z5ecl8K4K+JfKgyoPmfkP/wBHw94Lh+COIqBNcgILvf5V5r0udPaehYOqqIqIoVVFgo2tOdJd2TKVcEnhHCUw6hEFhzPNj1Y8zJJTrpyncPiQ3nO16/IQ0uxTcPUew0MjioesGzwWfWWV9yKD1G1gHb6R9apcAAXP9Y3E6d0adZm022kXWyALXe4C2A59SfKD43hEqUwbWO5Hvt9I3NY6STRcOwVwCP8AqYuNpps0bqmkeYcTwDI9ipFwCLgi6nYi/KVVTDWOmn97T0XtdRXKbfY2vqbX2v6zFsNDeITateDqglJWR8PUIGVhvaxO4/7k79TcqXAa1u/p8vet3ugvl35yMKYMtzXcsy5mzPlFTvaMB9lhzN7HU/WQ5Lk3UG9kC4amSpmCpUuhupvlUOpU321Gbl4GMxuHCfZUhxmUgtdNdvPTUa+cn03FJHulwVN9bG5sqkabAttzvH4SkatPM12sbgc+QOvkAPSZyypRUnwFibbIGJ4c3wRiCQUdwg1ObOEDMD4a2l92YT4eJd8xYOpI/eX5hfxFj7Su4zjlZVw+QJkcsutiwIVQMqi17C+Y6m1p3AO1Fg6G9r90/KQRY+U6Fmjjab4dGLwSyQdc7mrxPHghtkMr63aBz8oAhsHRo4oA95HPI7GxIOUnfUH2j6nZd/suD5z0YzU1cTy5wlB1JUVrcYrff+kfT45WHMHzEM/Z6sOQPkZM4P2fLMTWUhRawB+Y+Y5fzlZ5FCOpkJWPwfGww74JPRVJkyjjqbtkyt/EttpdYXCIgsiKBz0GvmecJWoB9CoPp+E53nlOL08iqK7PcwqtYSvxVN0cqFYjyOngfGHw6O32SPOebi1qVNO/4LNon5lKMuW7G1j52FrSFjsBk+W56/z8pZ4fDhO82rcvD+sGz5nZeWRrnoTt9FaexhbSp8ldLKBqcGaclssGVnQVKtYRYNYzF4tKVMu50HTcnkB4wSkTFEr8bx/DUjlaoGf7iAu3ssp2pYjFauWp0ztTU2JH77DX0EsMFwRKYsqgeQ/E85W74L6UuSl4/wAVSuEzU6iDv5Q1lNzlsxGulwNPrI2DwuZ8gbTKT3QDc5C1gD7RvHv/AJTDWyBVA6XUE2947Bo6r8RBohzNc6HUZQBbcWJtfX8eSbeo2SSiXHAqgTDKgIvnbP5nVfMZbS8oPMXheKL8Ri3cVzmBsMuhI2AAte406TaYJFABLZunT+shIo1uWmGFgT1iZtZU1+JsCQttDbXwjsPxRWNnFvHl78pVtFlFloXg/iSLiKxAuD3esF+sCWTIcSelfK308o/EvfXpKs1/GcpYjvectZGnuGLawyVAvebYa+2sAzCV3E+IKiEsfIdZzzjyax3KjtDxXPmO2Zjp4TP4jFFVswFiAVNraeEFjarPmIBsu/hc2EgBi4ynlqNeXOMWNpW+50KSXBd8Gqh3sN7MR4kKSB6yf2eYGsVa1yT/AGJUcKLUs9mt3DlsoYl2Ay5eS+J6XHO0seGCmiM7IzVDYJrcLr3na1tdVA5fMeQkZccXFqL3ZvhyuLbki37Q03Wmfhki1s37yNcEfhrIPBcc1NCum9rEgDw1vrr0k+lWxDCzrTpq65DUqlVBW4JOR/m1UbA2kHE1sOjHN/nkc1ulMsOhtmI31sJjHD/iUJos8knJ6e5FxtA4mrmYtmvZQL/KBawNrb66dTtB8Txq0EsrEvtl1YepP5GMxvHnfu5VRPuoD7FiSx9TID/DqCzG010K0mtkXhiyadnuSuDdoH+KpIvrpbQ+k9Sw3aNMi5kbNYX23955Tw7gzq6snfFwdN9+k1qK4OqsPQzoxaVJuBwda5NqMkbJePIfsP8AT+ctMPWDAEaXANjMPh6vUTQ0cXa3lOfrJ5GkkrVnFFJF9mnVexv0lWOILbecXiCnn9ZlDPVKhJFlUJZrnUn/AKj0phdTv+EBh66EXU3I30I/GPz3nfr2oRj3FVeQnr5TYbtc28soDe5t/HJhW8h4/CMULIBmXUX030OvkTLY3UrLqk9yIywZEkFYMidRgUCmVHaStkFJ2GZFqHON+XdPmO9LsYd+kHiuHmpTZGXRhblp0I8RKyTaovFpSTY7CYxGRWQgqRoR/ekmJUBmEfhuLwhORM6E30BYedhqp28POQavaXEDQIgP8Rt6XlFNLnY39LVw7JfahrYlyCO6FLdRoBr4ba+Mo/8AEdDdrA6W0PMGVdUszFmJJYkknmTGiiZnLS3Zt6MqLqniqZ+c+GnPxPWWeF44KICo+dTpk1BQAaFTt6eEy6YfwMkrgvCZvSu5X0ZeDXVOMI4Dg72J8DbUGNXiadZkTh2H/UaaTSlfM0WN90benxcDZhbmDqD6SWnE6Lj5sreek88yN0PuY74TDr7mNPzLemu5vTxFPvCF/wAUpouZnEwCq/j7mI0Hbcn3MV5ZPoo0+N7VqoulyfHbz0mYxXFHqsWdr39h4AcoJsGIJsN4S8VAh4pftRZ8N4saYKg3zXDaXFiCNj5nWPDC1ha1+gJ6jX+UrKdC0lobSs9+Dox9M63LF2W+YWB7ulzyHTbl1lsnHqq0mWmgRSe86L3yTqbv9m9thbaZ0mxOvWSaNSx+ZlBAViLg5SuVhYHUWuLc5nbR0Lp1W6D1a6s18tza2YsTc/ePjb8vXoy2JZRYhgMrahtSrWJJsDprygaLk5u6CW5kXy33tyB8YZKJJ9vpM5SSOqGJcA/1LOLWkHE8JddVvNXgOHsxGhmw4f2fULep7fzlMWXJKWmCv8GHVTxY423ueZ8CFRDnzMtjoNbnx8polx7nd2PrNnV7PUG+wPSQsR2cpIpfXTYX3PIepsJ6ccelM+fnleSVsoBVa9je/je+uolth8T3RLDEcARnLsTcn+mnpJeG4bRpjRcx6tqPYzPJp4Zn/BTtUBgs9uc0NZEO6j2Ebh8NQY5Sgvy8ZjGMG6FtEXhfEbAg7XkylxlDUCDY2Ga+hJ5Acx4zPdoMfQpv8NFtluXI2vpZd9QNb+njKmljBmurbWt562/Kc+bI4SqPbk3irieo0iJ3EnuyIQCARpcA6ab+UBWqMNCb+M9DHJXRzydjHMA0a9SDNSdJUcAIRQIBWhA0AKAILEcPo1Pnpo/+5QT7wgadvDVkp0ZviXZPCt8qFD+6x/A3mW4n2WendkGdfAd4ek9DrnWR7zKWKLRtDPOPc8rGH1sRb0kumnhPRqmGR/nRW81BPvBf4VQP7MfUfgZyz6ab4aO2PXR/cjAfql48YHwm9Tg9D7n/ALN/OHp8OojZF9bmY+1zeUX99j8M88/UD0jHwRHI+09QSig2RR6CFFugmi6SfdlH10e0TycYa/KPXAMdlJ9J6o1NTuoPoJ1aajYAeQk+0l5Hv1/z/Z5BiaZQ2ZSPMQPdM9exVNX7jBW0JsRf++couJdjqD6oTTPuPaWfTtcMQ69N7qjzipQI15QQE1eJ7EYhflKOPOx9jIbdmcSu9FvSx/AyrjJcpnfj6rE+6KZVPSS6dLTkffSWdDs9W503HmplxhOz5XVyFHiR+Ewm5PaKf2N31GJK219yjweDY7TT8K7OM2p0HU/l1krD1MNR3YMw9vaGq9qUHyoTLY+klN3ldLwuTg6j9Sf+uL7l5gsElMd0a9ef9JKBmObtU/2UHvBntNWP2VHpPQhGMI1BUjyJynOVydsiYjtPiXqNkfIuYhVCrcAGw1IJJlniKOOamjVCSqkPYBQbjVc2UdZF4Bw8VsWaxAABzkAaZzsQPO58xPRqVrWmKUpNpsltKqRjsP2nQtlqqUO2Yar681HvLR62mklcS4JSqKwyLqDY21U8iDKgJ8MBLWCgKB4DQazl6hSju3yE0+B71IL4jLZl01tfleRMfxFKfztYnYbk+QkGlx2m5y2Ya6XGhv6zkSm90SZfEYljU7++ZiTzNyc/1N4sNVysLNox9gNAfp9Za8Yw9PE1xSppkcgNUqd4ZbaEFNmY6WItve5g8B2adK65mU01N73O3+w7H+7yzyQS+N064ZtGUUj0zAH/ACUv/pp/9RH4hbpy5+Y2HttIi4teRFuUe9UWPlp53H5XnVhzRnwzlkQXMETHVDAlp6hUMrR4aRwY8NADh4/NI4aOzQBtQwNo9zG3gCAjhGiOkMsPvGtiUG7Aesp+J4aqdnAHnaUNXCkHvOp9SZVyoJGzGPpjd1950cSo/wConuJhzRH3h9ZxKYvqdJXWxRvE4jS/1E/5CMPEkY2R1awu1tfIX26+0yaYbD/aZz5KB+cn4B6CNlp57tp37W6jaVc2GiXw7Eu+MdmuFNlUHTuqNLD/AJH1mgJlQjrT+RBfe/jrr4bn3gK/GKg+xLxVcgvbzmcTHV+0lQbKJFbj9dugk2hRssVqNGtMpj8BUZ7Byb+MiDiFdyBm3NtusvUXKLXv1PMzHLlUV8yy2K9uBKi3epmbop28NpGfCW2N9OcsnMCEJNgLk6C05JZpPglNlJSqsr2PtyltRUML2nOLcKqIlOqyGztZTpr4HoeeskYKmFW3r7y+KU+JGstMlfc0PZimFRj1b8AJo0eZ/g7WBHrLdKknV8RXTsWCteQuI4QOpNtVBItvpyHXyhUqTrvN9px0syapnjvE2L1WZtCW2O4toBBfDJtl11Fudzyml7dYNVqCogtm38+sF2SXRzlzd4C5tYEa31nNHG1LSaN7WTgtSwIRr2AOnQQ1OjVO6EeZH85amrGfEif6dilJylZlqI9PBtzIHreTHYKu9zzP9OUA1SRsRU0muHpMeJ2kRY968YasiF5zPOxEFkGjg0jho4NJAfNFmgc07mgBGMbeMzRZoAUGI6iDDxwaAVmN4S7m6v6GVz8Hqj7N/IzThojUAlXFFkzLLwqqfsH6STS4DUPzFV+svGxaDnI1TiyCRpQsFR4Ag+ZyfIASfT4fSTZAT1Op+sqqnHegkKrxmodtJGmKG5pnsBtKPilbkLSrqY2o27mR2JO5JktkjHFzHJTnVEkIJUHKVlYN0Mt6FZCbte3O2595VYpO57SPSxBE8/qJNST7EWXFRhc22jUexuOWt+fpIKYqJsRMoyT4Fl5WxLGlbNmUZmykAAO/dJHU2Le8rqbyA2L1A5XEm03vsJ2wtoupFxg8Vklxh8WrbGZ2lScjRTJFPBPvcD1lJYpN2i6kjTpUhC8pKCFd3JkkYq202hCS5KSkiL2g4WtcKGdlK9LfnBYXDJRphE2HM6kk7knrHYrFEnUyG2Km8YJO+5W3VElnjA8inETnxpYoSXeAqPBtUgXeQgPLRpeCNSMLywLUNOhoHNO3gBw0WaCzRZoATNFmg80WaAFDTueADR2aAPeoZX4nEP4ydmjWUGQWKCo7HrB5T0mh+AvSIUV6SKBn8jdDF8NvumaIIvSPsvSNIszWVuh9pzI33T7TTXHQRZh0EULM0tNjyMMmGf7hmgBHSO+JFCykOAqEfLI/+DVeoHrNJ8SDd5WWOMuRZS0uCH7T+wkunwqmN7nzMlO8CzyiwQXCA8YSmPsiSqbKNgJXNUM6tWaKKXALhK86asqlrQgrSaBNepAPUgjUgalSKAypVN4L4kG7RhaSA2eLPAZpzNBUOXjGeBLxpeAFLxheCLRuaSD/2Q=='},
     '4': {'id': 4, 'link': 'http://127.0.0.1:5000/view/4', 'title': 'Quince', 'year': '2019', 'latitude': '37.79762', 'longitude': '-122.40337', 'city': 'San Francisco',
                'region': 'California', 'zipCode': '94133', 'cuisine': 'Contemporary', 'price': '$$$$', "wine": ["Margaux", "Screaming Eagle", "Château Latour", "Ridge"], 'description': 'Few people eat here. Is the food a good value? Few know the answer. This is the 4th sentence.',
                'url': 'data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAoHCBYVFRgSFRUYGBgYGBgZGBgYGBgYGBkYGRgZGRgYGBgcIS4lHB4rHxgYJjgmLC8xNTU1GiQ7QDs0Py40NTEBDAwMEA8QHhISHjQrJCExMTQ1MTQ0NDQ0NDE0NDY0NDE0NDQ0MTQ0NDQ0NDQ0NDE0NDQ0NDQ0NDQ1NDQ1NDQ/P//AABEIALUBFgMBIgACEQEDEQH/xAAcAAABBQEBAQAAAAAAAAAAAAAAAQIDBQYEBwj/xABBEAACAQIDBQQGCAQGAgMAAAABAgADEQQSIQUGMUFRImFxgQcTMpGhsRRCUmJywdHwM5Lh8RUjQ0SCslOiFhck/8QAGQEBAQEBAQEAAAAAAAAAAAAAAAECAwQF/8QAKxEAAgIBAwMCBQUBAAAAAAAAAAECEQMSITEEQVFhcRMiMpGhI0KBsdEF/9oADAMBAAIRAxEAPwC2arE9cJGySPLPks+5Gh9Vr8JPSJAvGUgLR9NtCJpEmSMbyJl17pw43FZDa878E+dR1giVKyVQCCpGh0I7jPDtsYQ069SnY6O1hbkTcfAie5FYmF2BRrOajIC44nqJ6MEqlXk8nVRuN+DxrZu7OJr+yhA6t+k2eyfRpexqsT3DQT1TD4FEFgo906QJ7T55ndj7n0KVgqLfrYXm6wuHVFCqLATlwKa3ljIUIQhACEIQAhGlo0vAHkwEjtJBIBYQhKAhEvFgBCEIAQhCAEIQgBGlY6EAaFikQvCQAIQBhKDzQJ1jGQTpZJx4mrlIvPlM+wt2Oprc2k3q4xNdRJ0HdCLJmc3pw7ZBUX6hufCS7CxRcKRL2vhw6lSLgixmUwNM0KppHhe6+E0+CxdqjXmlfW8XBV/VuDyOh8I3DNcSCuCTZdTzPISxdU0c3HVcWa6KBOXYlTOlie0uh/KWYoifRjJSSZ8qcXGTT7EuCblO6V6U7cDJQ7Dnfygh1ExheQGoY0tAJjViZ5zMTANAOpZIBOVKklV4BOIshDxweASQiAxZQJaLCEAIQhACEIQAhCEAIhgTGEwBbxrNGlokhRQ8IkIBhQukqt4aDNRcr7Si48pYq0c6X0POfNR9XdMod3tpesQE8eB8ZpEsdRMBVU4XElfqObjoCZtcBUzAERJaX6Mr3VnTbWU+3sJmX1i+0mo8OYl0zXkFVxw43gRbsp9l7RzICOMsq7WUa8eNplMSTQqug4HtKPmJe4TGrUUEHW3A8R5RVHSk9y43exOSqBwD6EfI/vrNoBPPEYghhoQbjrpN/haudFfqAZ68ErTR4OrjUlJdya0LRYTueMS0QCOjTAGkRjSGvtGknt1EXxYCcT7wYYf6qn8N2+UAsbSRVlG+81AcM58Ef9I1d6af2Kn8tvmZG0KNIiR4SZ4b1U/sP7h+skXeinzR/wCUfrJaLTL8LHWlEN6aHPOP+BPykg3nw3OoV/Ejj8pdSFMuDEBlYm8WFP8AuKXm4X5zupYpH1V1b8LA/Iy2iUTiLEiEygdCMvDNAHwjCYwmSwPYyNmgYkASLEhAHWhEEIKeeK95OgvxlXhsVdb9J108TfunzEfYcWys3rwOenmA7S6gxm7GOzoATqNDLXGkMhBPKYzYmJyVmQcCTNtao+xmKp0+5vWeRGoOQ85yLidCLyBseACOJ5Tmmzqo7HDvUgCpVHtKwHiDykuykR7NYqT0lTvRiGKJfm3ynfu5icygdJ0a+VMifKRoWSwsNJqd362aiov7JI+Oky1Q8rS23Xq2zpfoZ0wyqXueXqI3C/BqM0XNIs8M89h84kLRGeRM8iepJYMdicCgq1CEUEu5JsLkliSY5aAAsJW19sKXc30LsR3jMbQG2BNuNks7yltJCyWMhG0k6xxx6nnObibTJkpmdC0tJxLjx1jztIDnIolOpqYEq8e4GkK+1RKjF4sm8OIRz4upxv0lS9XW4t4jQyTG1zfyla9TmdJaI2XWH2/iKfsVqi+Dtb+Um0t8Lv8A41Lf5iVBfhURfmmUzDVcSesjWsbcZaJZ7Ds/0mA6VqHDi1Nr+Jyta3vmkwG+ODq6CsEP2anYPvOh8jPA8M19eH5yd6tjob+Mm42PpJHDC4IIPAg3Hvjp86YPb2IotmpVnQ9Fbs370PZPmJutj+kt1AGJpZxp26ej+aHQ+RHhLYPT4hlbsnblDErmo1Fe3FeDr+JDqJYykAxIsSAEIQgHjdMlGKnrOhMQRJtq0QKp7wDIVpAz57ij7cMnykgrlhaYzCv/APpP4j85uFCqD4GefYOrmxLfiPzm4LZnGcrkvc3hp3ESnhRePo1BkEY1fkJyO7K/eSiGp6fVM5t2BYXltVp51y9849lUyhamRqCfdym5fQYxVrZoQ9xOnYNe1fjxBErsNTZzlQeJPCd+Ew4pVAxcWF8xOgGkkLtMmfSotehrjWjGxEyW0N9MJSuDWDsPq0+2feNB5mZrGekvW1LD6dXex/lUH5z2rU+EfJbS5PTXxM5MeHelURCFdkdULcA7KQpNu+eRYv0hYtvZKU/wJc+9yflLHcveqtUxIpYiq1QOCFuFGVlBbgoA1Ab3Cc8uqEHJcpCLjJ0ULYtkJRuyykqwPEMpsQe8EERj7RPWde/1DJj6o4B8jj/ki5v/AGDHzmbep0nfHPVBS8qzjJU2i7obRPMzqXaZ75naLGd+Ha3GaZqJd09oMbWk7M7C3WV2FrC/CX2FxqW1E885tcI9OPHGXLONMK9uBkeIpsON5fHalMCVuN2ijcBOccsm+DrLFFLkzmJqWJldVqGWOLqBjcSrrT0xdnkkqY0dTEvrEt3wpzZzOxGyxvrJAakjNSSi2dXreskTEX4/sTgDXio5ihZbYPFsjCorEMpOUglWHLRlNwZ6Hu16Te2KWLHZJ7NVR2l10FRPrdMyi/3ec8tR4xRfX92kotn1HRrK6h0YMrC6spBBHUEcZJPB9zd8quDcI93ok2dOepHbQk6Pqe5rAdGHuGCxS1UWrTYMjgMpHMfkeRHIiCk8IQgHmO8Iy1RcfV/OcQcTVbw7MLoHAuV4gcbGZP6Mb2E8koOLPp4ZxlFDnbQ+Ex2z8CRXckaXuvnNViqbWY3sqIzubaKqqWZj5Dzma3Y2jnd85sWOZQTwW1sovEYvS2alOCkk+TUpVCprON8ag1PLyEbiXBFydOkz+3apdMiCy3uxHE9wmIw1M1lzKEbLUb2Uk4I7m54ZQPIkyLDb0rWrAGmKYIsDmzEnlm0Fpl0wp6ToeiFF9L9e+ep44uOk+bHPOM9R6tgKgt0md39xSvT+jKy52ZXsxt2UNzc+6Yxd5cSgyK+g4EqCR4GVFaozsXdizHizG5/tMYsDi7b4Oubqoyi0lyToEIN2KEDQWLXPQEcBH4mgEVHDq2e+i8R0vOV0seug8OEY6z1HgFvrxnVszFerq06t7ZHR/JWBPwvOMRwkaTVMvBvfSnQtiKNXk9HL5o7H5OJiAJud+n9ZgcBiTxK5W8Xpqx+NMzBI9zYAkngACSfADjPP0rfwkn2tfZm8n1M6UNtekU4oTow+wMbV0p4Wu1+fq3UfzEASzw/o92k3+2K/iemvwzT0bGdyrpY0DnJf8R6Ey6/+sdokfw0HjUWRVfRrtMf6Cn8NSn+ZEzSKm0VDbQ74DE35yevuTtFNWwlT/jlf/oTKnEYSvT/iUaifjR0/7CNKNamd/rBfXhInZZWhzAPNaTNnUza2EM4nP6yNZ5SHSz6wAuZzEyWgTAOgJ/aGWOQHgDpz14nl48fjJkp38+H9plsqVkGTTu5SZEsDe4EdVqACwHdG1GuAJm2zdJEZq8zy/OegeibeU06v0R2/y6ztkufYqWBAA5BwCNPrAdTfzaoYuFxDU3Wop7SMrqejqbofJrS0Zvc+rYSHB4gVESqODqrjwZQ35wgpyKsjq4NG9pFPkJMhikw6CtcGW37QJgMQEUC6qpsLaM6K3wJnitOn5T6B27gvX0KlHm6ED8XFfiBPFsTs802IP9DF9iO+ThVm43nYiX7xGrRI1tJgbDQ+XzkoWRGnYW/flOLEqTpJ6lS542/pJPU3Hy56e+aSI5WUVWjbjOcvL+rgiRwvx0lfiNnm9hxmjBXFyTI2edzYFl7RAsCNCL3seBHSde7+7lbHVfVUUsBq7nRKangWPE87DifeYKimQFiFUEkmwABJJ6ADjNvu/wCjDGYmz1bYenxu+rkdyA3H/Iieqbq7nYbAqCi56tu1WcAseoX7C9w87zTKZmzVGWwO5+HFKnga4NdKPbXPpdu1a4WwIAdhY93SaTAbJoURlo0adMfcRV+Qi1P4iHqCPdf9Z1iefBs5R8N/k6S3p+g60bHXmQ25v1h6LNQpsHr5sgU3CBtfabu0053FjO7Zk0O08eKCesZWZcwBy2uL6A2JF9bDziUNpJUQvTZWspIW9jexIVh9XhPGk3wxNVglSozoOy40CgkFgWGUZiCLcOI4y42ZtGxV1IRioLJmFxqDztmF7cp5MueWOSdWvye/B0sc0GrqXbw0ej7K2mKlIO7IGzMptoL3uoAJv7JE7nUEWIBHQi4nn2xtsUsKxNbMwJLIbZihYtmtc6A3C/3mj3f3h+khiyhCNVAN7rexJPUGej4kZJST2fH+HjlgnGTi1xyJtTc7A4gHPhqYJ+ugyP8AzLaYjbPokXVsLXIOvYq29wdRp5gz1IPfgYXmrOdHzXtbdrEYZitamV6E+yfwtwPDkZUOtp9Q4/BU66GlVRXRuKsLjxHQ94njO/u5X0T/ADqWZ6DNa/FqZPBWt9XkG8AdbX0pWRqjBWMkRiDFVe+deGA5900yDvUk2tof0nSlPKNTy0HIX7/dGBx/TujXr3Ovz/fUzBojqEE6fvrIg1vGKlzwjgt+MoOVwSY4CSvoDNH6PdgnF4pAwORCHfTTIpvlJ+81l8CekWSj3zY1EpQo0zxWlTU+IRQflCdkINFSHgakiEJys3Q5nmP3q2PmBqotxxYDiCePkePvmvKyNk6i4OhB4ESWxR46afSM9TpabLePdgpevh7leLINSvh1Ey6VOR+M6p3wcmitejrYj98514fDcBa/jOrEUlOoMscBhQwBBHhNWFE56GEHE9+n74yX6Kh4ge6Wpojz5fH3Tmrr1HjxmbKU1XZwqOEVRdjlA7yRYT1nYWyEwtJaKKBbViPrNzJ/fCYfd4D16E8M6nXx/UielAQRiWiZrRZwY17m3Kcc+ZYYambjFydEtfFKWUg3ynW3TSQbT29ToU2qvmsLAC2pY6Ko8ZU7UxaUKb1nYKFVtNBma1wouRcm08y23tGrXLlxmsEXIrLZMwOWyZ9S2ouGDDtXE+f0ufLknKdJJs7ThFI22N3kxmJ/gU/VUWFizMudgbk5TyuCBcDrY9MNVwmIo1FDqWYqQvaupyl2shY2591ufG89B2bXQohygrktlB9kqLFTbgQRa3dKjbNIPlZmb1aOoJFicx9kWtoORPxm49TNz3Wxwx6pypFTg9iZc9RAc9Ulxm4qe0GXTS19AfGcu29mMX9SGCgqCxQMS1vqkkAZetr8fGaBcVkRkosCXXOqMTmtm1Kg6i9iCOBsJx03dvbQ29rtFkuDwNtDbwE9OTqcU8dq012o9mjLiai915OzC7HIRHzqxYEvdS5bRQEAOgFg3v7zFxGEFslMKjrqyKWIJsG0DE8OGlpa4Sg5AzkG+XKovlGmgAPDSdX/AMfQual2LE3N2a1z0W9p8vqOpi9lz7dzpjk4yuxN2sQSg7RvzU3uOpB6D98ppFqHx/fWVmBo5CV6ajvv/b4yyp0mbuHxPhOeB5nP9Pb+jOdxbtkytcXkGLoJUR6bqGR1Kup4FSLETrZQBIC0+6nXJ46Pnfb+xGw1d6BPsMQDcXZTqjWHC4t8ZVaD9e+bnebbavialRXDpnKhWRGTKAEJBJuQct9bcZiKo5j3a6X5d87o5PkkRjzj6VO57vd3yFKZI8+HdOuglhIwPaiBrwEjZrR7NfnLbYO7FbFuBTQ5bjM7AhFHO55nukNFRs7ZtTEVFp00LsxsAPiT0E+gtz93EwNAU11drGo/Vug+6OXmecduxu1SwaZUAZz7TkC54aDoNOEvYAQgISgp8sXLJLRAs40bsQLArHWigSiyAqRqJR7X3YpV7ugCOensk+E0mWMZJQeUbQ2LWw5s6Ej7Q4HznJRdlOhPhznr7DSzAEdDKfHbsUKuq9hu7h7ppS8mdPgx2GxwOh6ec6LBted+EdtDc6uhzIc47uPulayVU0dGUjqNPjGxNy3o0spDd+lv33CbfZW0BUSxPbUdodfvDuMwGE2jycW75aUqxuKiHKeNxHBTcXkNRAdZXYTbAIs+n3h7J8ek6q1UEXBFjz4j3zh1Ol422rrsaherYxu/+DrVlVKAzKL3AQE57EKwubnjbu75hm2ViVsiUqmYWzdhtWC3Rrg27J0A85676mpmzZyw+zcAfKdOY21sOXtc58XH1soLSoqj1OEfNnlOzth48OwpipSD6uzDQGwuwW9ixINza+o6majB7DdfbZ3JUK+chlNuagABeJ0tzmsqU35FR4gn85EvrQRdVI6rcEeR4zM+sySfZfwdIJR4ozuI2OS2ZVtYAA9Nb6dOJ98r8NSDYhUu3FkYZmygi5JAJsNRfTjNhVq2daYJN+Itew7zylNtLZD5zWoAllIcqOZGtx97Thz+cwznOT8vg9uHJBpxyVutm/Je4ahZVDcVFr+Gl/OTopOii/y8zHbOpq6LUvcMoYDgBfkR1HDXpLNVA0E9mP8A58py1ZXz4PlTyU2vBx4bC2NzqbX7rnp7p2QnLjMclMXdwvdxJ8ANTPqQxxhGoo4uTk9yWq0w+++9C0EbD0jes4sSLf5atxJ++RwHn4pt3eKtVvTw49WvN2PbI+7bRfHj4TF/4eqdpzmY6kk3JN+N+Zm1He2Zb2pFMmGtYgnhqCNOYIHUcpyPhxe+gHITS/RalXspTPcAPiZZbN9HuJqkGoQi9/H3TVmdJhfV9P3/AFlrsvYGIxJAp02I6nQDxM9b2T6PcNSszg1G6t+k1eHw6IAqKFA5AWjcqVHnu7/ozRLPiWzn7Cmw8zPQcNhUpqERQqgWAAsJPaEUAEIWhKAhCEA4LRMsmywKzDRohywtJSsblkoo0CLaKBHWgERSRvTnTaJllBzLUYcdRHMqOLMAe4iSNTkbUoBwYjd+g/1APDT5SsfdK3sVGHcdRNCMw4GPWt1EUDNvsWsPst5kTkfZ2IU3XOh+4wt5g6H3TZrVEkFjGklmNo7RxKfxKCuB93I3mV0+E6qe8lO9nw1VO8LmH6/Caj1Y6RDQXoJzeGEuUvsXUyjTbeFb/UZe5kcfNZKNpYY/7hPM2lr9FT7I90T6En2B7hOcukxP9qLrfkrRi8N/508iBePXaOGUaOvlc/KWH0JPsD3CPGET7I903jwQx/Skg5t8lb/jVEDs5j+FDznO+3WPsUXP4gfkJeLh1+yJIKY6TtRkyr18XU4KVHdZfibmQrsKu5u2UHqSSZsgoi3EUQyVPdK/tuR1CgD4md+F3TwyG5TMerkt85e5oXloENHCIgsqgeAk8QCLKAhaEW0EAQhaLaAJaEWEFEhFhAOa0XLFEdaQDMsQrJLQtJQISsLSXLEyyFGWhaPtEywBtohWSWhaAQlI0pOi0MsA5jTiernVlhlgHMFPWOBbrJ8sMsAiDtFDt0kuSLlmiEec9IocyTLDLAGZjFF5JaFoAy0ULHWi2gDbRbR1oWlAgELR1osAbaLaLCAEIQgBCEIA2EIQCER0ISAWEIQAhCEAIQhAEhCEAAIsIQAhCEAIRYQBIsIQAhCEAW0W0IQBbRYQlAQhCAEIQgBEJhCAJFEWEECIYsIKMhCEA//Z'},
     '5': {'id': 5, 'link': 'http://127.0.0.1:5000/view/5', 'title': 'Atelier Crenn','year': '2019', 'latitude': '37.79835', 'longitude': '-122.43586', 'city': 'San Francisco',
                       'region': 'California', 'zipCode': '94123', 'cuisine': 'Contemporary', 'price': '$$$$', "wine": ["Margaux", "Screaming Eagle", "Château Latour", "Ridge"], 'description': 'Few people eat here. Is the food a good value? Few know the answer. This is the 4th sentence.',
                       'url': 'https://guide.michelin.com/us/en/california/san-francisco/restaurant/atelier-crenn'},
     '6': {'id': 6, 'link': 'http://127.0.0.1:5000/view/6', 'title': 'The French Laundry', 'year': '2019', 'latitude': '38.40443', 'longitude': '-122.36474', 'city': 'San Francisco',
                            'region': 'California', 'zipCode': '94599', 'cuisine': 'Contemporary', 'price': '$$$$', "wine": ["Margaux", "Screaming Eagle", "Château Latour", "Ridge"], 'description': 'Few people eat here. Is the food a good value? Few know the answer. This is the 4th sentence.',
                            'url': 'https://guide.michelin.com/us/en/california/san-francisco/restaurant/the-french-laundry'},
     '7': {'id': 7, 'link': 'http://127.0.0.1:5000/view/7', 'title': 'The Restaurant at Meadowood', 'year': '2019', 'latitude': '38.52025', 'longitude': '-122.46479',
                                     'city': 'San Francisco', 'region': 'California', 'zipCode': '94574',
                                     'cuisine': 'Contemporary', 'price': '$$$$', "wine": ["Margaux", "Screaming Eagle", "Château Latour", "Ridge"], 'description': 'Few people eat here. Is the food a good value? Few know the answer. This is the 4th sentence.',
                                     'url': 'https://guide.michelin.com/us/en/california/san-francisco/restaurant/the-restaurant-at-meadowood'},
     '8': {'id': 8, 'link': 'http://127.0.0.1:5000/view/8', 'title': 'SingleThread', 'year': '2019', 'latitude': '38.612164', 'longitude': '-122.869705', 'city': 'San Francisco',
                      'region': 'California', 'zipCode': '95448', 'cuisine': 'Contemporary', 'price': '$$$$', "wine": ["Margaux", "Screaming Eagle", "Château Latour", "Ridge"], 'description': 'Few people eat here. Is the food a good value? Few know the answer. This is the 4th sentence.',
                      'url': 'https://guide.michelin.com/us/en/california/san-francisco/restaurant/singlethread'},
     '9': {'id': 9, 'link': 'http://127.0.0.1:5000/view/9', 'title': 'Alinea', 'year': '2019', 'latitude': '41.91328', 'longitude': '-87.64798', 'city': 'Chicago',
                'region': 'Chicago', 'zipCode': '60614', 'cuisine': 'Contemporary', 'price': '$$$$', "wine": ["Margaux", "Screaming Eagle", "Château Latour", "Ridge"], 'description': 'Few people eat here. Is the food a good value? Few know the answer. This is the 4th sentence.',
                'url': 'https://guide.michelin.com/us/en/illinois/chicago/restaurant/alinea'},
     '10': {'id': 10, 'link': 'http://127.0.0.1:5000/view/10', 'title': 'Geranium', 'year': '2019', 'latitude': '55.70393', 'longitude': '12.57197', 'city': 'København',
                  'region': 'Denmark', 'zipCode': '2100 Ø', 'cuisine': 'Creative', 'price': '$$$$', "wine": ["Margaux", "Screaming Eagle", "Château Latour", "Ridge"], 'description': 'Few people eat here. Is the food a good value? Few know the answer. This is the 4th sentence.',
                  'url': 'data:image/jpeg;base64,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'}
     }
]

current_id = 3
data = [
    {'1': {'id': 1, 'title': 'Amador', 'year': '2019', 'latitude': '48.25406', 'longitude': '16.35915', 'city': 'Wien',
           'region': 'Austria',
           'zipCode': '1190', 'cuisine': 'Creative', 'price': '$$$$$',
           "wine": ["Margaux", "Screaming Eagle", "Château Latour", "Ridge"],
           'description': 'Few people eat here. Is the food a good value? Few know the answer. This is the 4th sentence.',
           'url': 'https://axwwgrkdco.cloudimg.io/v7/mtp-cf-images.s3-eu-west-1.amazonaws.com/images/max/9d89fb7e-a8ff-4bb3-a8e0-cdf29003e7dc.jpg?width=1000',
           'link': 'http://127.0.0.1:5000/view/1'
            },
     '2': {'id': 2, 'title': 'Manresa', 'year': '2019', 'latitude': '37.22761', 'longitude': '-121.98071',
           'city': 'South San Francisco',
           'region': 'California', 'zipCode': '95030', 'cuisine': 'Contemporary', 'price': '$$$$',
           "wine": ["Margaux", "Screaming Eagle", "Château Latour", "Ridge"],
           'description': 'Few people eat here. Is the food a good value? Few know the answer. This is the 4th sentence.',
           'url': 'https://s.hdnux.com/photos/60/22/02/15351870/7/1236x0.jpg',
           'link': 'http://127.0.0.1:5000/view/2'},
     '3': {'id': 3, 'title': 'Benu', 'year': '2019', 'latitude': '37.78521', 'longitude': '-122.39876',
           'city': 'San Francisco',
           'region': 'California', 'zipCode': '94105', 'cuisine': 'Asian', 'price': '$$$$',
           "wine": ["Margaux", "Screaming Eagle", "Château Latour", "Ridge"],
           'description': 'Few people eat here. Is the food a good value? Few know the answer. This is the 4th sentence.',
           'url': 'data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAoHCBUVEhgVFRUYGRgYGhgYGhoaGBoaGBgYGBgZGRgYGRgcIS4lHB4rHxgYJjgmKy8xNzU1GiQ7QDs0Py40NTEBDAwMEA8QHxISHzQrJSs0NDQ0NjQ0NDQ0NDQ1NDQ0NDY0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NjQ0NDQ0NP/AABEIALABHgMBIgACEQEDEQH/xAAcAAABBQEBAQAAAAAAAAAAAAADAAIEBQYBBwj/xABAEAACAQIEAwYDBAgGAgMBAAABAgADEQQSITEFQVEGImFxgZETMqFCUrHBBxRDYoLR4fAVI1NykvEzojSy0hb/xAAaAQEAAwEBAQAAAAAAAAAAAAAAAQIDBAUG/8QALBEAAgIBAwMCBQQDAAAAAAAAAAECEQMSITEEQVETFCJhgZGxBUJxoSMyUv/aAAwDAQACEQMRAD8A8fyxWj8sWWCRlogI/LEBAGETloS04VgDCJy0JaK0AHaK0JadyQSByxZYXJFkgAssWWFtOFYAPLOWhcsWWACtFaEKzmWADnLR5E5aCBsU7OQBRRRQQKKKKAKKKKAKKKKAKKKKAKKKKAKKKKAT8kWSSckWSARsk78OSckctMQCGUnTTkr4XhOmgYBC+HO5JMFKFTAu3yox8lJ/KCSuyGd+HLul2fxLfLRf/iR+MlU+yOLb9iw8yP5xZJmjTi+HNcvYfFn7CjzaGTsFiba5P+R/lFkGK+HOtTm3H6PsQd2Qep/lOj9Htf76fWLBhMsRSbo/o9r/AH0+sa/6P64BJenYAknXQDcyLJMMUnCk2VHsLWdA6VKTq2oKsbH6Tj9g8UOSH+L+kWDF5I0pNfU7FYsfYB8mEg1uyWLX9gx8iD+cWDNlY2XFbgWJX5qDj+G/4SvqYR1+ZHHmrD8RJsUR5y0cYoFDbTs6IoFDTFOxQRRyKK0UECiiigCiiigCiiigGl+B0BhaOCZjZUcnwBP4T1DC9ncOn2Mx6sb/AE2lpRoKuiqB5ACAeY4XsrXf9my+LELLbD9g3Pz1FXwAJM36rHhYBkcN2EoD53dvUAfSWdDsphV/ZBv9xLfjL4LHBYBAo8Lop8tJB5KJKWiBsAPIQXFOIJh6RqvfKCB3QCdTbQEjz9I/h+Op10z0nDrtpuD0YbqfAyNromnVhcsWWGyyj4z2mw+GW7OD1sb9drXzG45ba3IkkchKnGKS4g0HJVgFIJHcOYXAvfQ+eksss8m452mTEVVqLSe62G6oGCkkXHfJgMRx1VLZkqNmF7DFVsoe+oIVgMu+3hM4zdtP6G0oKk4/U9VOPoh2Q1UDJ8wLAFdAdb+BExWA7RU8MHL1lqpny5EdWc3J/wAxBe2XqL+1tcWOM0r3OFpX6kO1/Msxkul2gofawNIj93u2/wDUyHu0/BMVScfJ6FS7aYRtjU2v/wCJzyvuLj6zg7YYR1Ib4gVgRc0nIKkWvdb/AFmIw3EqdSoL5xTzCyO2YgH5xcBRbYC+vjIvF6K0cQ6qXQZrpclGCk929uY2PlKPM9VUa+3pJ2XXCeMDCd4OWpNmypbV1W1m/cJB3PTaaj/+uwzUs6FmbT/LykPc+emmuoMwFfDOKqVP1hXNwRkqo9+ZFlvlHW4t5yXj1IZKhYBnvdVRVVQrDTuqLknnzt4aZ+qoKkb+g8j1yW35PUaZDqGXUEAj1kGpxKmuIGHJIdlzDTunfu3+9YXnnGIxTJUZ6bsilg4sct7WsSoJHLxhsRxHENUXEPTzFCrfEVSuaxBUFhddttpdZ9S2Rh7ZJu2emMkC+HU7qD6CZbG9t0qUstJWSo1wQwuVGxII0v0Osu+yjO2ETOSbEqCd8o2uefPWba03pMpYZRhrfF0Or8Jov81JD5qJV4jslhG/YqL/AHdPwmoZIxklqMbMLif0f4Y/Izp63/GVOJ/R4w+SsD4Mv5iemmnGFIoWeP4nsVi02RWH7ra+xlPieFV0+ek4/hJHuNJ7qacG9IHcQLPACIp7djOBYep89JD45Rf3lDjOweHb5CyHwNx7GCTy+ctNjjewdddUZHHT5TM9i+E16fz0nXxtce40ixRXxRxWcIkkUciitFBB9KAR6rEoj1EASrHhZ1RHAQBAToEo+PdpUwrBWpu5K5u7lAAJtuxBO3IG2l95DwHbvCu4R89NjtnAym+3eBIHrK6ldWW0Sq6LvjXDhicO9Em2caH7rA3U25i4HpeeQUcc+AxZszh1DpUAPdz2YLcD51Bs2tpqO0/bpiWo4QEWurVe7e9yCEGot+97TCU8KXLZmYljmYkk3bXVidzqdfEyk5RTvwaR1JV5LXH9pMViLg1Hy6b5L+gUBeV7hbjrK/DcOJ3trbTcvqNNNzcg28po+G8PFdhSop8qjMT8qm1jc63ubkdfCbvgnAaOH+yGqHeowF/IdBOd5JSL1GKMRgeyr5MxTKSRoeQ8vaSanZdrHb2npDYe87SwovrMvTld2R6nyPGsX2dOtk3PKVVfgjrpqATqNvee5VaSXIy+ttZW4zgyMCdDfraWU5x43Fp8o8aXCunpG18YX/8AJcsNLkknbxnomN7NMb5Bf8JkeJ8GZG7ykekLJFv4tjVW+CFwykA+ZeQvvy9Zc8UqLUKFAQQoBB2vc3C87a85nhQZDcH1ljhcYGsrWuNOl/G/XWUyJt6ludMJ2tLHcSogrlBN8uoa90e/eA29tdzC8DwzZWUldAWOvJR9TrtOs7A5hqddTruNd/ODpuQtibWN7W1uRqb+g/u8jVcaEZOEm0SKop50y/KfnupAQnSygMS2XQ3vr066js52kCjJWyqgvZwLAFmLWYDQDU7DQDpe2TqUiGKsLNp9dRGG9gOl/wC7+kQyOLtFJx1xpnqz8SoBM/xUy/eDqR7gwtGorqHRgytqCDcGeZ0cMPiB3KoWFtQLlxZbFV+W9tz585fcIw71nNGo10Qtamj5VUHUPUKDv95rizDVSDbSdcM7lKqOefTqMbTNgUjCklFI34c6TkIxSMKSYacaUgEI04xkk0pBulgSdAIBBqKALnQRlSj1G+vI+4lpTwakhnAYjUAi6i+xtzP4SwZFZMpVfQWnL7qLk0i9UjB4/s3hqt89JQeq90+4max/YIamlU/hcfmJ6hisGALqLSC1KbxkpK0Vs8W4h2dxFL56Zt95e8PpKk0zPeXpSqxvAMPVN3pi/UaE+dpYWbBSIRTKNMUYVcU0kguljgJUpjDCLjjAJXEOG066ZKqBhyOzKeqnkZ49icKhqvTWxCVHUNbvMFawY8uWlupnovaHjpo4dmvZmBVRrckixsRsRe9/Dxnm+AQoM29/pOfNX1OjFJpEulgEBCjdvc+Z5ecl8K4K+JfKgyoPmfkP/wBHw94Lh+COIqBNcgILvf5V5r0udPaehYOqqIqIoVVFgo2tOdJd2TKVcEnhHCUw6hEFhzPNj1Y8zJJTrpyncPiQ3nO16/IQ0uxTcPUew0MjioesGzwWfWWV9yKD1G1gHb6R9apcAAXP9Y3E6d0adZm022kXWyALXe4C2A59SfKD43hEqUwbWO5Hvt9I3NY6STRcOwVwCP8AqYuNpps0bqmkeYcTwDI9ipFwCLgi6nYi/KVVTDWOmn97T0XtdRXKbfY2vqbX2v6zFsNDeITateDqglJWR8PUIGVhvaxO4/7k79TcqXAa1u/p8vet3ugvl35yMKYMtzXcsy5mzPlFTvaMB9lhzN7HU/WQ5Lk3UG9kC4amSpmCpUuhupvlUOpU321Gbl4GMxuHCfZUhxmUgtdNdvPTUa+cn03FJHulwVN9bG5sqkabAttzvH4SkatPM12sbgc+QOvkAPSZyypRUnwFibbIGJ4c3wRiCQUdwg1ObOEDMD4a2l92YT4eJd8xYOpI/eX5hfxFj7Su4zjlZVw+QJkcsutiwIVQMqi17C+Y6m1p3AO1Fg6G9r90/KQRY+U6Fmjjab4dGLwSyQdc7mrxPHghtkMr63aBz8oAhsHRo4oA95HPI7GxIOUnfUH2j6nZd/suD5z0YzU1cTy5wlB1JUVrcYrff+kfT45WHMHzEM/Z6sOQPkZM4P2fLMTWUhRawB+Y+Y5fzlZ5FCOpkJWPwfGww74JPRVJkyjjqbtkyt/EttpdYXCIgsiKBz0GvmecJWoB9CoPp+E53nlOL08iqK7PcwqtYSvxVN0cqFYjyOngfGHw6O32SPOebi1qVNO/4LNon5lKMuW7G1j52FrSFjsBk+W56/z8pZ4fDhO82rcvD+sGz5nZeWRrnoTt9FaexhbSp8ldLKBqcGaclssGVnQVKtYRYNYzF4tKVMu50HTcnkB4wSkTFEr8bx/DUjlaoGf7iAu3ssp2pYjFauWp0ztTU2JH77DX0EsMFwRKYsqgeQ/E85W74L6UuSl4/wAVSuEzU6iDv5Q1lNzlsxGulwNPrI2DwuZ8gbTKT3QDc5C1gD7RvHv/AJTDWyBVA6XUE2947Bo6r8RBohzNc6HUZQBbcWJtfX8eSbeo2SSiXHAqgTDKgIvnbP5nVfMZbS8oPMXheKL8Ri3cVzmBsMuhI2AAte406TaYJFABLZunT+shIo1uWmGFgT1iZtZU1+JsCQttDbXwjsPxRWNnFvHl78pVtFlFloXg/iSLiKxAuD3esF+sCWTIcSelfK308o/EvfXpKs1/GcpYjvectZGnuGLawyVAvebYa+2sAzCV3E+IKiEsfIdZzzjyax3KjtDxXPmO2Zjp4TP4jFFVswFiAVNraeEFjarPmIBsu/hc2EgBi4ynlqNeXOMWNpW+50KSXBd8Gqh3sN7MR4kKSB6yf2eYGsVa1yT/AGJUcKLUs9mt3DlsoYl2Ay5eS+J6XHO0seGCmiM7IzVDYJrcLr3na1tdVA5fMeQkZccXFqL3ZvhyuLbki37Q03Wmfhki1s37yNcEfhrIPBcc1NCum9rEgDw1vrr0k+lWxDCzrTpq65DUqlVBW4JOR/m1UbA2kHE1sOjHN/nkc1ulMsOhtmI31sJjHD/iUJos8knJ6e5FxtA4mrmYtmvZQL/KBawNrb66dTtB8Txq0EsrEvtl1YepP5GMxvHnfu5VRPuoD7FiSx9TID/DqCzG010K0mtkXhiyadnuSuDdoH+KpIvrpbQ+k9Sw3aNMi5kbNYX23955Tw7gzq6snfFwdN9+k1qK4OqsPQzoxaVJuBwda5NqMkbJePIfsP8AT+ctMPWDAEaXANjMPh6vUTQ0cXa3lOfrJ5GkkrVnFFJF9mnVexv0lWOILbecXiCnn9ZlDPVKhJFlUJZrnUn/AKj0phdTv+EBh66EXU3I30I/GPz3nfr2oRj3FVeQnr5TYbtc28soDe5t/HJhW8h4/CMULIBmXUX030OvkTLY3UrLqk9yIywZEkFYMidRgUCmVHaStkFJ2GZFqHON+XdPmO9LsYd+kHiuHmpTZGXRhblp0I8RKyTaovFpSTY7CYxGRWQgqRoR/ekmJUBmEfhuLwhORM6E30BYedhqp28POQavaXEDQIgP8Rt6XlFNLnY39LVw7JfahrYlyCO6FLdRoBr4ba+Mo/8AEdDdrA6W0PMGVdUszFmJJYkknmTGiiZnLS3Zt6MqLqniqZ+c+GnPxPWWeF44KICo+dTpk1BQAaFTt6eEy6YfwMkrgvCZvSu5X0ZeDXVOMI4Dg72J8DbUGNXiadZkTh2H/UaaTSlfM0WN90benxcDZhbmDqD6SWnE6Lj5sreek88yN0PuY74TDr7mNPzLemu5vTxFPvCF/wAUpouZnEwCq/j7mI0Hbcn3MV5ZPoo0+N7VqoulyfHbz0mYxXFHqsWdr39h4AcoJsGIJsN4S8VAh4pftRZ8N4saYKg3zXDaXFiCNj5nWPDC1ha1+gJ6jX+UrKdC0lobSs9+Dox9M63LF2W+YWB7ulzyHTbl1lsnHqq0mWmgRSe86L3yTqbv9m9thbaZ0mxOvWSaNSx+ZlBAViLg5SuVhYHUWuLc5nbR0Lp1W6D1a6s18tza2YsTc/ePjb8vXoy2JZRYhgMrahtSrWJJsDprygaLk5u6CW5kXy33tyB8YZKJJ9vpM5SSOqGJcA/1LOLWkHE8JddVvNXgOHsxGhmw4f2fULep7fzlMWXJKWmCv8GHVTxY423ueZ8CFRDnzMtjoNbnx8polx7nd2PrNnV7PUG+wPSQsR2cpIpfXTYX3PIepsJ6ccelM+fnleSVsoBVa9je/je+uolth8T3RLDEcARnLsTcn+mnpJeG4bRpjRcx6tqPYzPJp4Zn/BTtUBgs9uc0NZEO6j2Ebh8NQY5Sgvy8ZjGMG6FtEXhfEbAg7XkylxlDUCDY2Ga+hJ5Acx4zPdoMfQpv8NFtluXI2vpZd9QNb+njKmljBmurbWt562/Kc+bI4SqPbk3irieo0iJ3EnuyIQCARpcA6ab+UBWqMNCb+M9DHJXRzydjHMA0a9SDNSdJUcAIRQIBWhA0AKAILEcPo1Pnpo/+5QT7wgadvDVkp0ZviXZPCt8qFD+6x/A3mW4n2WendkGdfAd4ek9DrnWR7zKWKLRtDPOPc8rGH1sRb0kumnhPRqmGR/nRW81BPvBf4VQP7MfUfgZyz6ab4aO2PXR/cjAfql48YHwm9Tg9D7n/ALN/OHp8OojZF9bmY+1zeUX99j8M88/UD0jHwRHI+09QSig2RR6CFFugmi6SfdlH10e0TycYa/KPXAMdlJ9J6o1NTuoPoJ1aajYAeQk+0l5Hv1/z/Z5BiaZQ2ZSPMQPdM9exVNX7jBW0JsRf++couJdjqD6oTTPuPaWfTtcMQ69N7qjzipQI15QQE1eJ7EYhflKOPOx9jIbdmcSu9FvSx/AyrjJcpnfj6rE+6KZVPSS6dLTkffSWdDs9W503HmplxhOz5XVyFHiR+Ewm5PaKf2N31GJK219yjweDY7TT8K7OM2p0HU/l1krD1MNR3YMw9vaGq9qUHyoTLY+klN3ldLwuTg6j9Sf+uL7l5gsElMd0a9ef9JKBmObtU/2UHvBntNWP2VHpPQhGMI1BUjyJynOVydsiYjtPiXqNkfIuYhVCrcAGw1IJJlniKOOamjVCSqkPYBQbjVc2UdZF4Bw8VsWaxAABzkAaZzsQPO58xPRqVrWmKUpNpsltKqRjsP2nQtlqqUO2Yar681HvLR62mklcS4JSqKwyLqDY21U8iDKgJ8MBLWCgKB4DQazl6hSju3yE0+B71IL4jLZl01tfleRMfxFKfztYnYbk+QkGlx2m5y2Ya6XGhv6zkSm90SZfEYljU7++ZiTzNyc/1N4sNVysLNox9gNAfp9Za8Yw9PE1xSppkcgNUqd4ZbaEFNmY6WItve5g8B2adK65mU01N73O3+w7H+7yzyQS+N064ZtGUUj0zAH/ACUv/pp/9RH4hbpy5+Y2HttIi4teRFuUe9UWPlp53H5XnVhzRnwzlkQXMETHVDAlp6hUMrR4aRwY8NADh4/NI4aOzQBtQwNo9zG3gCAjhGiOkMsPvGtiUG7Aesp+J4aqdnAHnaUNXCkHvOp9SZVyoJGzGPpjd1950cSo/wConuJhzRH3h9ZxKYvqdJXWxRvE4jS/1E/5CMPEkY2R1awu1tfIX26+0yaYbD/aZz5KB+cn4B6CNlp57tp37W6jaVc2GiXw7Eu+MdmuFNlUHTuqNLD/AJH1mgJlQjrT+RBfe/jrr4bn3gK/GKg+xLxVcgvbzmcTHV+0lQbKJFbj9dugk2hRssVqNGtMpj8BUZ7Byb+MiDiFdyBm3NtusvUXKLXv1PMzHLlUV8yy2K9uBKi3epmbop28NpGfCW2N9OcsnMCEJNgLk6C05JZpPglNlJSqsr2PtyltRUML2nOLcKqIlOqyGztZTpr4HoeeskYKmFW3r7y+KU+JGstMlfc0PZimFRj1b8AJo0eZ/g7WBHrLdKknV8RXTsWCteQuI4QOpNtVBItvpyHXyhUqTrvN9px0syapnjvE2L1WZtCW2O4toBBfDJtl11Fudzyml7dYNVqCogtm38+sF2SXRzlzd4C5tYEa31nNHG1LSaN7WTgtSwIRr2AOnQQ1OjVO6EeZH85amrGfEif6dilJylZlqI9PBtzIHreTHYKu9zzP9OUA1SRsRU0muHpMeJ2kRY968YasiF5zPOxEFkGjg0jho4NJAfNFmgc07mgBGMbeMzRZoAUGI6iDDxwaAVmN4S7m6v6GVz8Hqj7N/IzThojUAlXFFkzLLwqqfsH6STS4DUPzFV+svGxaDnI1TiyCRpQsFR4Ag+ZyfIASfT4fSTZAT1Op+sqqnHegkKrxmodtJGmKG5pnsBtKPilbkLSrqY2o27mR2JO5JktkjHFzHJTnVEkIJUHKVlYN0Mt6FZCbte3O2595VYpO57SPSxBE8/qJNST7EWXFRhc22jUexuOWt+fpIKYqJsRMoyT4Fl5WxLGlbNmUZmykAAO/dJHU2Le8rqbyA2L1A5XEm03vsJ2wtoupFxg8Vklxh8WrbGZ2lScjRTJFPBPvcD1lJYpN2i6kjTpUhC8pKCFd3JkkYq202hCS5KSkiL2g4WtcKGdlK9LfnBYXDJRphE2HM6kk7knrHYrFEnUyG2Km8YJO+5W3VElnjA8inETnxpYoSXeAqPBtUgXeQgPLRpeCNSMLywLUNOhoHNO3gBw0WaCzRZoATNFmg80WaAFDTueADR2aAPeoZX4nEP4ydmjWUGQWKCo7HrB5T0mh+AvSIUV6SKBn8jdDF8NvumaIIvSPsvSNIszWVuh9pzI33T7TTXHQRZh0EULM0tNjyMMmGf7hmgBHSO+JFCykOAqEfLI/+DVeoHrNJ8SDd5WWOMuRZS0uCH7T+wkunwqmN7nzMlO8CzyiwQXCA8YSmPsiSqbKNgJXNUM6tWaKKXALhK86asqlrQgrSaBNepAPUgjUgalSKAypVN4L4kG7RhaSA2eLPAZpzNBUOXjGeBLxpeAFLxheCLRuaSD/2Q==',
           'link': 'http://127.0.0.1:5000/view/3'}
    }
]

current_id = 4
sales = [{
    "id": 1,
    "salesperson": "James D. Halpert",
    "client": "Shake Shack",
    "reams": 1000
},
{
    "id": 2,
    "salesperson": "Stanley Hudson",
    "client": "Toast",
    "reams": 4000
},
{
    "id": 3,
    "salesperson": "Michael G. Scott",
    "client": "Computer Science Department",
    "reams": 10000
},
]
current_id_names = 10
names = [
    "Shake Shack",
    "Toast",
    "Computer Science Department", "Teacher's College",
    "Starbucks",
    "Subsconsious",
    "Flat Top",
    "Joe's Coffee",
    "Max Caffe",
    "Nussbaum & Wu",
    "Taco Bell",
]


# ROUTES

@app.route('/hi')
def hello():
   return 'Hi hi hi hi hi hi hi hi hi'

@app.route('/')
def top_restaurants():
    print(data[0]['1']['title'])
    return render_template('top_restaurants.html', data=data)

@app.route('/edit/<count>')
def restaurant_page(count=None):
    global restaurant
    restaurant = restaurants[0][count]
    return render_template('restaurant_page_editable.html', restaurant=restaurant)

@app.route('/view/<count>')
def restaurant_edit_page(count=None):
    global restaurant
    restaurant = restaurants[0][count]
    return render_template('restaurant_page.html', restaurant=restaurant)

@app.route('/search_results')
def search_results(name=None):
    global restaurant2
    restaurant2 = restaurants
    return render_template('search_resultsblank.html', data=restaurant2)

@app.route('/search_results/<query>')
def search_results_with_query(query=None):
    print("query", query)

    global restaurant_titles_in_search_results
    global restaurant_regions_in_search_results
    global restaurant_cusines_in_search_results
    global titles
    global region
    global userquery
    global match_count
    global cusines

    restaurant_titles_in_search_results = []
    restaurant_regions_in_search_results = []
    restaurant_cusines_in_search_results = []
    reslink = []
    restaurant_objects = restaurants[0]
    userquery = query

    title_match_count = 0
    region_match_count = 0
    cusine_match_count = 0
    for restaurant in restaurant_objects:
        titles = restaurant_objects[restaurant]["title"]
        regions = restaurant_objects[restaurant]["region"]
        cusines = restaurant_objects[restaurant]["cuisine"]

        if not (titles.lower().find(query.lower()) == -1):
            title_match_count += 1
            restaurant_titles_in_search_results.append(restaurant_objects[restaurant]) #will pass in the object
        if not (regions.lower().find(query.lower()) == -1):
            region_match_count += 1
            restaurant_regions_in_search_results.append(restaurant_objects[restaurant]) #will pass in the object
        if not (cusines.lower().find(query.lower()) == -1):
            cusine_match_count += 1
            restaurant_cusines_in_search_results.append(restaurant_objects[restaurant]) #will pass in the object
    match_count = title_match_count + region_match_count + cusine_match_count
    # print("matchcount", title_match_count, region_match_count,match_count)
    if title_match_count == 0:
        restaurant_titles_in_search_results.append('no match')
    if region_match_count == 0:
        restaurant_regions_in_search_results.append('no match')
    if cusine_match_count == 0:
        restaurant_cusines_in_search_results.append('no match')



    return render_template('search_results.html', match_count = match_count, data=restaurant_titles_in_search_results, cusine_matched = restaurant_cusines_in_search_results, regions_matched=restaurant_regions_in_search_results, reslink = reslink, query=userquery)

@app.route('/welcome')
def welcome():
    return render_template('top_restaurants.html', data=data)

@app.route('/people')
def people():
    return render_template('people.html', data=data)

@app.route('/infinity')
def infinity():
    return render_template('log_sales.html', data=sales)

# AJAX FUNCTIONS

# ajax for people.js
@app.route('/add_name', methods=['GET', 'POST'])
def add_name():
    global data 
    global current_id


    json_data = request.get_json()   
    name = json_data["name"] 
    
    # add new entry to array with 
    # a new id and the name the user sent in JSON
    current_id += 1
    new_id = current_id 
    new_name_entry = {
        "name": name,
        "id": current_id

    }
    restaurants.append(new_name_entry)

    #send back the WHOLE array of data, so the client can redisplay it
    return jsonify(data = data)




# The TA helped me with the code below. He said my code was very close and he made some adjustments that he said were ok for me to include

@app.route('/edit/<id>', methods=['GET', 'POST'])
def save_title():

    global restaurants
    global new_restaurant_title


    print("in save new rest data")
    restaurants_dictionary = restaurants[0]

    new_restaurant_title = request.get_json()

    restaurants_dictionary['2']["title"] = new_restaurant_title



    return jsonify(data = restaurants)

@app.route('/save_sale', methods=['GET', 'POST'])
def save_sale():
    global sales
    global restaurants
    global sale_data
    global current_id_res
    global clients

    print("in save sale server page")
    restaurants_dictionary = restaurants[0]
    index_of_restaurant_to_add = current_id_res + 1
    string_index_of_restaurant_to_add = str(index_of_restaurant_to_add)

    restaurant_input = request.get_json()
    # add key value for new restaurant
    restaurants_dictionary.setdefault(string_index_of_restaurant_to_add)
    restaurants_dictionary['11'] = restaurant_input
    print("new index", restaurants_dictionary['11'])
    print(restaurants)



    return jsonify(sales = sales)

@app.route('/delete_sale', methods=['GET', 'POST'])
def delete_sale():
    global sales
    global index

    sale = request.get_json()
    print(sale)
    sales.remove(sale)

    # send back the WHOLE array of data, so the client can redisplay it
    return jsonify(sales = sales)


if __name__ == '__main__':
   app.run(debug = True)




