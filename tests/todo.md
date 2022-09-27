create new test functions for generate difference file step-by-step 
open file + read file(+ strip) + print (or save to file)

для вложенных структур сделать склейку списка с переносом строк

получается нужно сцепить элементы списка рекурсивно. если элемент списка строка, то 
''.join([i + '\n' for i in list_ if type(i) is str else join_lines(i)])
