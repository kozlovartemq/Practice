select F1.X, F1.Y from Functions AS F1
Inner Join Functions AS F2
ON F1.X = F2.Y AND F2.X = F1.Y
group by F1.X, F1.Y                                     /* HAVING need to use, because it can interact with GROUP BY            */
having F1.X < F1.Y or (count(F1.X)>1 AND F1.X = F1.Y)   /* first expr uses to remove the second values of a pair from the list  */
order by F1.X                                           /* second expr uses to find pairs with the same x,y (F1.X = F1.Y)       */
