
srcpath = "C:/Users/Lenovo/Desktop/yz/1/"
srcFile = "cpst1.csv"
dstFile = "out"


def main():
    count = 0
    file_size = 200 * 1024 * 1024
    eof = False
    with open(srcpath + srcFile, 'rb') as f_source:
        while True:
            f_source.seek(file_size * count, 0)
            chunk_data = f_source.read(file_size)
            if len(chunk_data) < file_size:
                eof = True
            with open("{0}{1}_{2}.csv".format(srcpath, dstFile, count), 'wb+') as f_dest:
                print("creating {0} file".format(count))
                f_dest.write(chunk_data)
                count += 1
            if eof:
                print("file cut finished\n")
                return


if __name__ == '__main__':
    main()
