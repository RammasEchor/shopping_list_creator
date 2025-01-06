import gkeepapi

master_token = "aas_et/AKppINbKPwXNEfydfSOzRM-sp_P9fRuGxJ-T23DHjVrVO_QleAoTk7lFQf91dyvD1I1_2w7iMYyXsgI6Aa-n79Yy34g_J9SHwJ8caQ2LKmRgprX8IKgkIr9vWXNeF7zEkwIOivISPGPcf_juQjjFCslZGheu30FgzKFQXbM-lwBIhYyRfLX9cNHuVGSyVee0cW8ysHoxvvLQc9lYo7x-1u0="

gkeepapi.node.DEBUG = True
keep = gkeepapi.Keep()
keep.authenticate("luis.nieto.palacios1996@gmail.com", master_token)


def createListsInKeep(lists):
    listToCreate = []
    for name, itemList in lists.items():
        if len(itemList) < 1:
            continue

        for cant in itemList.values():
            listToCreate.append((cant, False))

        print(name)
        print(listToCreate)
        keep.createList(name, listToCreate)
        listToCreate.clear()

    keep.sync()
