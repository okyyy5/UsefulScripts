class Settings():
    def __init__(self):
      self.dry_run = False
      self.semester_weeks = 12

    def change_dry_run(self, value):
        self.dry_run = value

    def change_semester_weeks(self, value):
        self.semester_weeks = value

__settings__ = Settings()
__app_name__ = "UniFolderCreator"
__version__ = "0.1.0"



    