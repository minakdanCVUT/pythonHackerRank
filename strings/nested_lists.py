def secondMin(scores : list) -> float:
    m_min = 100
    second_min = 100 
    for element in scores:
        if m_min > element:
            second_min = m_min
            m_min = element
        if second_min > element and element != m_min:
            second_min = element
    return second_min
        

if __name__ == '__main__':
    end_list_names = []
    end_list_scores = []
    iterator = 0
    for _ in range(int(input())):
        name = input()
        score = float(input())
        end_list_names.insert(iterator, name)
        end_list_scores.insert(iterator, score)
        iterator += 1
    
    min_score = secondMin(end_list_scores)
    names_list = []
    for i in range(0, len(end_list_scores)):
        if min_score == end_list_scores[i]:
            names_list.append(end_list_names[i])
    names_list.sort()
    for name in names_list:
        print(name)
        
