def hash(key_list):
    hash_size = 10

    rslt = [None] * 20
    status = ["empty"] * 20

    for i in range(0, len(key_list)):
        j = 0
        while(1):
            hash_value = (key_list[i] + j) % hash_size

            if status[hash_value] == "empty": 
                rslt[hash_value] = key_list[i]
                status[hash_value] = "occupied"
                break
            else:
                j += 1

    return(rslt)


def hash_search(hashing_data, target_key):
    hash_size = 10
    j = 0
    while(1):
        tmp = (target_key + j) % hash_size

        if target_key == hashing_data[tmp]:
            ans = tmp
            break
        else:
            j += 1
    
    return(ans)


if __name__ == "__main__":
    key_list = [12,2,3,13]
    hashing_data = hash(key_list)
    print("ハッシュ法で作成したリストは{0}".format(hashing_data))

    rslt_3 = hash_search(hashing_data, 3)
    rslt_2 = hash_search(hashing_data, 2)
    print("3のindexは{0}".format(rslt_3))
    print("2のindexは{0}".format(rslt_2))