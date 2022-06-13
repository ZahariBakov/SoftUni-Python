def loading_bar(bar_volume):
    if bar_volume == 100:
        return "100% Complete!\n[%%%%%%%%%%]"
    else:
        return f"{bar_volume}% [{'%' * (bar_volume // 10)}{'.' * (10 - (bar_volume // 10))}]\nStill loading..."


number = int(input())
print(loading_bar(number))
