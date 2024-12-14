from datetime import datetime



dates = {
    "The Moscow Times": "Wednesday, October 2, 2002",
    "The Guardian": "Friday, 11.10.13",
    "Daily News": "Thursday, 18 August 1977",
  }

formats = {
    "The Moscow Times": "%A, %B %d, %Y",
    "The Guardian": "%A, %d.%m.%y",
    "Daily News": "%A, %d %B %Y",
  }



def main() -> None:
  for newspaper, date in dates.items():
    print(datetime.strptime(date, formats[newspaper]))



main()
