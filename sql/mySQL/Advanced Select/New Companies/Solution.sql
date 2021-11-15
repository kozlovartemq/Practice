SELECT Company.Company_code, company.founder, 
COUNT(distinct LEAD_MANAGER.LEAD_MANAGER_code), /* distinct - interact only with non-duplicate data */
COUNT(distinct Senior_Manager.Senior_Manager_code),
COUNT(distinct Manager.Manager_code),
COUNT(distinct Employee.Employee_code)
FROM COMPANY, LEAD_MANAGER, Senior_Manager, Manager, Employee 
WHERE   Company.COMPANY_code = Lead_Manager.COMPANY_code and
        Company.COMPANY_code = Senior_Manager.COMPANY_code and
        Company.COMPANY_code = Manager.COMPANY_code and
        Company.COMPANY_code = Employee.COMPANY_code
group by Company.COMPANY_code, company.founder
order by Company.COMPANY_code 
