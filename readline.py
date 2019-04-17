def data_loader(file_path, batch_size):
    path_list = []

    with open(file_path) as file:
        for line in file:
            if len(path_list) < batch_size:
                path_list.append(line.strip().split(' '))
            else:
                yield path_list
                path_list = []

        yield path_list

if __name__ == '__main__':
    read_gen = data_loader('sample_text.txt', 3)
    
    for lst in read_gen:
        print(lst)


