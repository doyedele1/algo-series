'''
    Explanation:
        shops - dictionary. {movie: sortedList(price, shop)}
        shop_movie - dictionary. {(shop, movie): price}
        rented - sortedList. (price, shop, movie)

        TC:
            __init__: O(nlogn)
            search: O(logn)
            rent: O(logn)
            drop: O(logn)
            report: O(logn)
        
        SC: 
            __init__: O(n)
            search: O(1)
            rent: O(1)
            drop: O(1)
            report: O(1)
'''
from collections import defaultdict
from sortedcontainers import SortedList
from typing import List

class MovieRentingSystem:
    def __init__(self, n: int, entries: List[List[int]]):
        self.shops = defaultdict(SortedList)
        self.shop_movie = {}
        self.rented = SortedList()

        for shop, movie, price in entries:
            self.shops[movie].add((price, shop))
            self.shop_movie[shop, movie] = price

    def search(self, movie: int) -> List[int]:
        if movie not in self.shops:
            return []

        result_shops = []
        for price, shop in self.shops[movie][:5]:
            result_shops.append(shop)
        return result_shops

    def rent(self, shop: int, movie: int) -> None:
        price = self.shop_movie[shop, movie]
        self.shops[movie].remove((price, shop))
        self.rented.add((price, shop, movie))

    def drop(self, shop: int, movie: int) -> None:
        price = self.shop_movie[(shop, movie)]
        self.shops[movie].add((price, shop))
        self.rented.remove((price, shop, movie))

    def report(self) -> List[List[int]]:
        result_report = []
        for price, shop, movie in self.rented[:5]:
            result_report.append([shop, movie])
        return result_report

# Your MovieRentingSystem object will be instantiated and called as such:
# obj = MovieRentingSystem(n, entries)
# param_1 = obj.search(movie)
# obj.rent(shop,movie)
# obj.drop(shop,movie)
# param_4 = obj.report()