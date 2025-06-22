from fpdf import FPDF

# Create PDF document
class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 14)
        self.set_text_color(0, 70, 130)
        self.cell(0, 10, 'SQL for Data Analysis Curriculum (2025 Edition - Microsoft Standard)', 0, 1, 'C')
        self.ln(2)

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.set_text_color(0)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(1)

    def chapter_body(self, body):
        self.set_font('Arial', '', 11)
        self.set_text_color(0)
        self.multi_cell(0, 8, body)
        self.ln()

pdf = PDF()
pdf.add_page()
pdf.set_auto_page_break(auto=True, margin=15)

# Content from the document
content = """
BEGINNER LEVEL (Weeks 1-4)

Week 1: Introduction to SQL
- What is SQL?
- Importance of SQL in Data Analysis
- Types of SQL Databases (MySQL, SQL Server, PostgreSQL, etc.)
- Setting up Microsoft SQL Server & SQL Server Management Studio (SSMS)
- Understanding Databases, Tables, Rows, and Columns

Week 2: Basic SQL Syntax
- SELECT Statement
- Filtering with WHERE clause
- Sorting with ORDER BY
- LIMIT and TOP keyword
- Aliases using AS

Week 3: Filtering and Logical Operators
- Comparison Operators (=, <, >, <=, >=, <>)
- Logical Operators (AND, OR, NOT)
- BETWEEN, IN, LIKE
- NULL Values and IS NULL

Week 4: Basic Functions & Expressions
- Arithmetic operations
- String functions: CONCAT, UPPER, LOWER, LEN
- Date functions: GETDATE, DATEPART
- Aggregate functions: COUNT, SUM, AVG, MIN, MAX
- GROUP BY and HAVING

INTERMEDIATE LEVEL (Weeks 5-8)

Week 5: Data Aggregation and Joins
- GROUP BY Revisited
- HAVING vs WHERE
- INNER JOIN
- LEFT JOIN, RIGHT JOIN
- FULL OUTER JOIN

Week 6: Subqueries and Nested Queries
- Subqueries in SELECT, FROM, and WHERE clauses
- Correlated Subqueries
- EXISTS and NOT EXISTS

Week 7: Data Cleaning & Transformation
- Data Types and Type Conversion
- CASE Statements
- COALESCE and NULLIF
- Using CAST and CONVERT
- Handling Duplicates with DISTINCT and ROW_NUMBER

Week 8: Data Import and Export
- Importing CSV/Excel into SQL Server
- Exporting Results to Excel
- Using the SQL Server Import and Export Wizard

ADVANCED LEVEL (Weeks 9-12)

Week 9: Advanced SQL Functions
- Window Functions (OVER, RANK, DENSE_RANK, NTILE)
- CTEs (Common Table Expressions)
- Recursive CTEs
- PIVOT and UNPIVOT

Week 10: Performance Tuning
- Indexing Basics
- Execution Plans
- Query Optimization Tips
- Avoiding Common Pitfalls

Week 11: Data Analysis Use Cases
- Sales Analysis
- Customer Segmentation
- Product Performance Analysis
- Time Series Analysis using SQL

Week 12: Building Reports & Dashboards
- Creating Views
- Using Stored Procedures
- Connecting SQL Server to Power BI
- Automating SQL Queries in Power BI

BONUS: Microsoft Certification Preparation (Optional)
- Microsoft Certified: Azure Data Fundamentals (DP-900)
- Microsoft Certified: Data Analyst Associate (PL-300)

Practice Projects & Assignments
- Real-life datasets for practice (Sales, HR, Finance)
- Weekly assignments and mini-projects
- Capstone project for SQL Data Analysis

Tools Used
- Microsoft SQL Server
- SSMS (SQL Server Management Studio)
- Power BI (Integration)
- Excel (Data Import/Export)

Learning Duration: 3 Months (12 Weeks)
Target Audience: Beginners to aspiring Data Analysts
"""

# Add content to PDF
pdf.chapter_body(content)

# Save PDF
pdf_path = "SQL_Data_Analysis_Curriculum_2025.pdf"
pdf.output(pdf_path)
