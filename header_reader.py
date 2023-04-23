from jawa.cf import ClassFile


class HeaderReader:
    def __init__(self, file_name):
        self.file_name = file_name
        self.class_file = None
        self.class_headers = None
        self.run()

    def run(self):
        self.read_file()
        self.get_info()
        for k, v in self.class_headers.items():
            print(f'{k}:{v}')

    def read_file(self):
        print(self.file_name)
        with open(self.file_name, "rb") as f:
            self.class_file = ClassFile(f)

    def get_info(self):
        self.class_headers = {"magic_number": '0x{:X}'.format(self.class_file.MAGIC),
                              "minor_version": self.class_file.version.minor,
                              "major_version": self.class_file.version.major,
                              "constant_pool_count": self.class_file.constants.raw_count-1,
                              "access_flags": self.class_file.access_flags.flags,
                              "this_class": self.class_file.this.name.value,
                              "super_class": self.class_file.super_.name.value,
                              "interfaces": self.class_file.interfaces,
                              "fields": [i.name.value for i in self.class_file.fields._table] if len(
                                  self.class_file.fields._table) > 0 else None,
                              "methods": len(self.class_file.methods._table),
                              "attributes": len(self.class_file.attributes._table)}

