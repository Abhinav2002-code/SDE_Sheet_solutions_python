SELECT Visits.customer_id, COUNT(Visits.visit_id) as count_no_trans
From Visits
LEFT JOIN Transactions
ON Visits.visit_id = Transactions.visit_id
WHERE Transactions.visit_id IS NULL
GROUP BY Visits.customer_id