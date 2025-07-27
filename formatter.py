def print_table(data,headers):
    if not data:
        print("No search results")
        return

    column=[max(len(str(row.get(h,'')))for row in data +[{h: h}])for  h in headers]

    header_line=" | ".join(h.ljust(w) for h,w in zip(headers,column))
    print(header_line)
    print("_"*len(header_line))

    for row in data :
        row_str=" | ".join(str(row.get(h,'')).ljust(w) for h,w in zip(headers,column) )
        print(row_str)

def paginate_results(data, headers,page_size=10):
    if not data:
        print("No results found.")
        return

    index=0
    total_pages=(len(data)+page_size-1)//page_size
    while True:
        index=max(0, min(index, (total_pages-1)*page_size))
        page=data[index:index+page_size]
        print_table(page, headers)
        current_page=index//page_size+1
        print(f"\nPage {current_page} of {total_pages}")
        print("\nOptions: [N]next | [P]previous | [M]menu | [Q]quit")
        choice_pag=input("Coice: ").strip().lower()
        if choice_pag=="n":
            if index + page_size<len(data):
                index+=page_size
            else:
                print("End of result")
        elif choice_pag=="p":
            if index - page_size >=1:
                index -= page_size
            else:
                print("This is first page.")
        elif choice_pag=="m":
            return
        elif choice_pag=="q":
            exit()
        else:
            print("Invalid input.")