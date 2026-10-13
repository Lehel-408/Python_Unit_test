def add_five(a: int) -> int:
    """Hozzáad 5-öt a megkapott 'a' egész számhoz."""
    return a + 5

def squared(a: float) -> float:
    """Négyzetre emeli a megkapott 'a' tizedestörtet."""
    return a*a

def add(a: float, b: float) -> float:
    """Összeadja a megkapott 'a' és 'b' tizedestörteket."""
    return a + b

def to_upper(s: str) -> str:
    """A kapott 's' stringet nagybetűsre állítja."""
    return s.upper()

def concat(s1: str, s2: str) -> str:
    """Összefűzi a megkapott 's1' és 's2' string-eket."""
    return s1 + s2

def str_contains(s: str, c: str) -> bool:
    """Megvizsgálja, hogy az 's' string tartalmazza-e a 'c' stringet."""
    return c in s

def list_sum(l: list[float]) -> float:
    """Összeadja az 'l' tizedestörteket tartalmazó lista elemeit."""
    s = 0

    for e in l:
        s += e
    
    return s

def count_fours(l: list[int]) -> int:
    """Megszámolja hányszor szerepel az 'l' egész számokat tartalmazó listában a 4-es szám."""
    c = 0

    for e in l:
        if e == 4:
            c += 1
    
    return c

def list_add_five(l: list[int]) -> list[int]:
    """Az 'l' egész számokat tartalmazó lista elemeihez hozzáad 5-öt."""
    l2 = []

    for e in l:
        l2.append(e + 5)
    
    return l2

def get_second(l: list[int]) -> int:
    """Visszaadja a kapott 'l' lista második elemét."""
    return [1]

def swap_elements(l: list[int]) -> list[int]:
    """Az 'l' kételemű listában felcseréli az elemeket."""
    return [l[1], l[0]]

def list_contains(l: list[int], a: int) -> bool:
    """Megvizsgálja, hogy az 'a' egész szám szerepel-e az 'l' listában."""
    return a in l

def split_by(s: str, d: str) -> list[str]:
    """Feldarabolja az 's' stringet a 'd' elválasztó karakter mentén."""
    l = s.split(d)
    return l

def parse_numbers(s: str, d: str) -> list[int]:
    """Feldarabolja az 's' egész számokat tartalmazó string-et a 'd' elválasztó karakter mentén, és visszaadja a string-nek megfelelő listát."""
    l = s.split(d)
    l2 = []

    for e in l:
        l2.append(int(e))
    
    return l2

def parse_rows(s: str, d: str) -> list[list[int]]:
    """Az 's' több sorból álló, egész számokat tartalmazó string-et beolvassa egy 2 dimenziós listába."""
    l = []
    rows = s.split('\n')
    for r in rows:
        row = r.split(d)

        parsed_row = []
        for e in row:
            parsed_row.append(int(e))
        
        l.append(parsed_row)
    
    return l

def calc_avgs(l: list[list[int]]) -> list[float]:
    """Egy kétdimenziós, egészeket tartalmazó listához kiszámolja a soronkénti átlagot."""
    avgs = []

    for r in l:
        s = 0
        c = 0

        for e in r:
            s += e
            c += 1
        
        avgs.append(s / c)
    
    return avgs