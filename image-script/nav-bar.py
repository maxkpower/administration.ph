import os
from bs4 import BeautifulSoup

# Define the updated navbar HTML as a string
updated_navbar = '''
<nav class="navbar navbar-expand-lg">
    <div class="container">
        <!-- Logo Start -->
        <a class="navbar-brand" href="{prefix}index.html">
            <img src="{prefix}images/logo.svg" alt="Logo">
        </a>
        <!-- Logo End -->

        <!-- Navbar Toggler Start -->
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
        <!-- Navbar Toggler End -->

        <!-- Main Menu Start -->
        <div class="collapse navbar-collapse main-menu" id="navbarNav">
            <div class="nav-menu-wrapper">
                <ul class="navbar-nav mr-auto" id="menu">
                    <li class="nav-item"><a class="nav-link" href="{prefix}index.html">Home</a></li>
                    <li class="nav-item"><a class="nav-link active" href="{prefix}about.html">About Us</a></li>
                    <li class="nav-item dropdown">
                        <a class="nav-link dropdown-toggle" href="#" id="servicesDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">Services</a>
                        <div class="dropdown-menu dropdown-menu-wide p-3" aria-labelledby="servicesDropdown">
                            <div class="container-fluid">
                                <div class="row">
                                    <!-- Accounting Column -->
                                    <div class="col-md-4">
                                        <h6 class="dropdown-header">Accounting</h6>
                                        <a class="dropdown-item d-flex align-items-center" href="{prefix}services/bookkeeping.html">
                                            <span class="material-icons mr-2">receipt</span> Bookkeeping and Accounting
                                        </a>
                                        <a class="dropdown-item d-flex align-items-center" href="{prefix}services/tax.html">
                                            <span class="material-icons mr-2">calculate</span> Tax Planning and Preparation
                                        </a>
                                        <a class="dropdown-item d-flex align-items-center" href="{prefix}services/reporting.html">
                                            <span class="material-icons mr-2">bar_chart</span> Financial Reporting and Analysis
                                        </a>
                                        <a class="dropdown-item d-flex align-items-center" href="{prefix}services/payroll.html">
                                            <span class="material-icons mr-2">attach_money</span> Payroll Management
                                        </a>
                                        <a class="dropdown-item d-flex align-items-center" href="{prefix}services/retirement.html">
                                            <span class="material-icons mr-2">elderly</span> Retirement Planning
                                        </a>
                                    </div>
                                    <!-- Relocation Services Column -->
                                    <div class="col-md-4">
                                        <h6 class="dropdown-header">Relocation Services</h6>
                                        <a class="dropdown-item d-flex align-items-center" href="{prefix}services/relocation.html">
                                            <span class="material-icons mr-2">flight_takeoff</span> Relocation Assistance
                                        </a>
                                        <a class="dropdown-item d-flex align-items-center" href="{prefix}services/accommodation.html">
                                            <span class="material-icons mr-2">home</span> Accommodation and Settling-in Support
                                        </a>
                                        <a class="dropdown-item d-flex align-items-center" href="{prefix}services/visa.html">
                                            <span class="material-icons mr-2">airplane_ticket</span> Residency and Visa Assistance
                                        </a>
                                    </div>
                                    <!-- Outsourcing Column -->
                                    <div class="col-md-4">
                                        <h6 class="dropdown-header">Outsourcing</h6>
                                        <a class="dropdown-item d-flex align-items-center" href="{prefix}services/administrative-support.html">
                                            <span class="material-icons mr-2">support_agent</span> Administrative Support
                                        </a>
                                        <a class="dropdown-item d-flex align-items-center" href="{prefix}services/company-incorporation.html">
                                            <span class="material-icons mr-2">business_center</span> Business Incorporation
                                        </a>
                                        <a class="dropdown-item d-flex align-items-center" href="{prefix}services/compliance.html">
                                            <span class="material-icons mr-2">gavel</span> Regulatory Compliance
                                        </a>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </li>
                    <li class="nav-item"><a class="nav-link" href="{prefix}blog.html">Blog</a></li>
                </ul>
            </div>
            <!-- Let’s Start Button Start -->
            <div class="header-btn d-inline-flex">
                <a href="{prefix}contact.html" class="btn-default">Contact us</a>
            </div>
            <!-- Let’s Start Button End -->
        </div>
        <!-- Main Menu End -->

        <div class="navbar-toggle"></div>
    </div>
</nav>
'''

def update_navbar_in_html(file_path):
    """Update the navbar in the given HTML file."""
    # Determine the prefix based on the file's directory depth
    depth = len(os.path.relpath(file_path, start='.').split(os.sep)) - 1
    prefix = '../' * depth

    with open(file_path, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')

    # Find the existing navbar
    navbar = soup.find('nav', class_='navbar')

    # If a navbar exists, replace it with the updated navbar
    if navbar:
        new_navbar_soup = BeautifulSoup(updated_navbar.format(prefix=prefix), 'html.parser')
        navbar.replace_with(new_navbar_soup)

        # Write the updated HTML back to the file
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(str(soup))
        print(f'Updated navbar in: {file_path}')
    else:
        print(f'No navbar found in: {file_path}')

def update_navbars_in_project(directory):
    """Recursively update navbars in all HTML files in the given directory."""
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                update_navbar_in_html(file_path)

# Update navbars in all HTML files in the current project directory
update_navbars_in_project('.')
