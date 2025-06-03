python source for creating template program python3 on Linux shell


usage: template.py [-h] [-m] [-o] file
template.py: error: the following arguments are required: file

template.py -h

usage: template.py [-h] [-m] [-o] file

positional arguments:
  file             create a python template file of given name

options:
  -h, --help       show this help message and exit
  -m, --main       add tags [if __name__ == "__main__"] to file
  -o, --overwrite  overwrite the file if it exists

  example:
  template.py test.py -m     # add tags [ if __name__ == "__main__" ]
create test.py with the following data

         #!/usr/bin/env python3
         # coding: utf-8
         #
         # @Autor....: Laudemir Oliveira
         # @E-mail...: laudemir.oliveira@gmail.com
         # @Date.....: 02-06-2025 - Mon - 22:16
         # @Version..: 2025-153
         #
        #

        def main():
            #TODO your code
            print("Hello World!")
    
    
        if __name__ == "__main__":
            main()

  
  template.py test.py -o -m    # overwrite the file if it exists

