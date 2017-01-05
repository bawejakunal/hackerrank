"""
https://www.hackerrank.com/challenges/lisa-workbook
"""

def main():
    """
    calculate special problems per chapter
    """
    n, k = map(int, raw_input().strip().split())
    chapters = map(int, raw_input().strip().split())
    prev = 0 #end of previous chapter
    current = 0#end of current chapter
    special = 0

    for problems in chapters:
        current = prev + (problems / k)
        if problems % k > 0:
            current += 1

        first = 1 #first problem on a page
        for page in xrange(prev + 1, current + 1):
            #special condition for last page of chapter
            if page == current and (problems % k) > 0:
                last = first + (problems % k) - 1
            else:
                last = first + k - 1
            if first <= page <= last:
                special += 1
            first = last + 1

        prev = current

    print special

if __name__ == '__main__':
    main()
