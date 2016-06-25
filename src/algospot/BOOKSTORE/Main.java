package algospot.BOOKSTORE;

import java.util.Collections;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.Scanner;

public class Main {

    private static int globalMin = Integer.MAX_VALUE;
    public static void main(String[] args) {
        // TODO Auto-generated method stub
        /*
		String[] inputs = new String[]{
				"5000 500 6000 1200 5500 550", 
				"3000 300 3000 1000 3500 350", 
				"1500 0 2000 500 5500 550", 
				"5000 500 5500 1500 2000 100" 	
		};*/

        Scanner sc = new Scanner(System.in);
        BookStore[] bookstores; //= new BookStore[]{new BookStore(), new BookStore(), new BookStore()};
        int T = Integer.parseInt(sc.nextLine().trim());
        for (int i = 0; i < T; i++) {
            globalMin = Integer.MAX_VALUE;
            String line = sc.nextLine().trim();
            int bookCounts = Integer.parseInt(line.split(" ")[0]);
            int storeCounts = Integer.parseInt(line.split(" ")[1]);
            bookstores = new BookStore[storeCounts];
            for (int q = 0; q < storeCounts; q++) bookstores[q] = new BookStore();
            for (int j = 0; j < bookCounts; j++) {
                String input = sc.nextLine().trim();
                String[] splits = input.split(" ");
                for (int k = 0; k < splits.length; k = k + 2) {
                    int price = Integer.parseInt(splits[k]);
                    int point = Integer.parseInt(splits[k + 1]);
                    bookstores[k / 2].add(new Book(price, point));
                }
            }

            for (BookStore bookstore : bookstores) {
                bookstore.min();
            }

            System.out.println(globalMin);
        }
		
		
		/*
		for(String input : inputs){
			String[] splits = input.split(" ");
			for(int i=0; i<splits.length; i=i+2){
				int price = Integer.parseInt(splits[i]);
				int point = Integer.parseInt(splits[i+1]);
				bookstores[i/2].add(new Book(price, point));
			}
			
			int min = Integer.MAX_VALUE;
			for(BookStore bookstore : bookstores){
				int price = bookstore.min();
				if(price < min){
					min = price;
				}
			}
			
			System.out.println(min);
		}*/


    }

    public static class BookStore {
        private List<Book> books = new ArrayList();

        public void add(Book book) {
            books.add(book);
        }

        public void min() {

            Collections.sort(books, new Comparator<Book>() {
                @Override
                public int compare(Book o1, Book o2) {
                    if (o1.point == o2.point)
                        return 0;
                    else if (o1.point > o2.point)
                        return -1;
                    else
                        return 1;
                }
            });



            int pay = books.get(0).price;
            int remainPoint = books.get(0).point;

            for (int i=1; i<books.size(); i++) {
                Book book = books.get(i);
                if(book.price >= remainPoint) {
                    pay += book.price - remainPoint;
                    remainPoint = book.point;
                } else {
                    remainPoint = remainPoint - book.price + book.point;
                }
            }

            if(globalMin > pay)
                globalMin = pay;

        }
    }

    public static class Book {
        public final int point;
        public final int price;

        public Book(int price, int point) {
            super();
            this.price = price;
            this.point = point;
        }
    }

}