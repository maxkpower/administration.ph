import os
import re

footer_template = """
<!-- Footer Start -->
<footer class="main-footer">
    <div class="container">
        <div class="row">
            <div class="col-lg-12">
                <!-- Footer About Start -->
                <div class="footer-about">
                    <div class="row">
                        <div class="col-lg-5">
                            <!-- Footer Logo Start -->
                            <div class="footer-logo">
                                <img src="{path_prefix}images/footer-logo.svg" alt="Administration.ph Logo">
                            </div>
                            <!-- Footer Logo End -->
                        </div>

                        <div class="col-lg-7">
                            <!-- Footer Title Start -->
                            <div class="footer-title">
                                <h2>Trusted by Businesses and Individuals Across the Country</h2>
                            </div>
                            <!-- Footer Title End -->
                        </div>
                    </div>
                </div>
                <!-- Footer End Start -->

                <!-- Footer Body Start -->
                <div class="footer-body">
                    <div class="row">
                        <div class="col-md-4 col-6">
                            <!-- Footer Links Start -->
                            <div class="footer-links">
                                <h2>Quick Links</h2>
                                <ul>
                                    <li><a href="{path_prefix}index.html">Home</a></li>
                                    <li><a href="{path_prefix}about.html">About Us</a></li>
                                    <li><a href="{path_prefix}services.html">Services</a></li>
                                    <li><a href="{path_prefix}contact.html">Contact Us</a></li>
                                </ul>
                            </div>
                            <!-- Footer Links End -->
                        </div>

                        <div class="col-md-4 col-6">
                            <!-- Footer Links Start -->
                            <div class="footer-links">
                                <h2>Blog Posts</h2>
                                <ul>
                                    <li><a href="{path_prefix}blog/accounting-tips-for-freelancers.html">Accounting Tips for Freelancers</a></li>
                                    <li><a href="{path_prefix}blog/how-to-pay-taxes.html">How to Pay Taxes</a></li>
                                    <li><a href="{path_prefix}blog/taxes-as-freelancer.html">Taxes as a Freelancer</a></li>
                                    <li><a href="{path_prefix}blog/vat-for-freelancers.html">VAT for Freelancers</a></li>
                                </ul>
                            </div>
                            <!-- Footer Links End -->
                        </div>

                        <div class="col-md-4">
                            <!-- Footer Contact Start -->
                            <div class="footer-contact">
                                <h2>Company Information</h2>
                                <ul class="company-info">
                                    <li>
                                        <span class="material-icons">location_on</span>
                                        Lot 4, Block 7, Unit 1, Filamer Subd, Bgy. Sicsican, Puerto Princesa City, 5300
                                    </li>
                                    <li>
                                        <span class="material-icons">business</span>
                                        CLEOPATRA SIRV PH HOLDINGS, INCORPORATED
                                    </li>
                                    <li>
                                        <span class="material-icons">person</span>
                                        Representative: MELINDA V. ACALA
                                    </li>
                                    <li>
                                        <span class="material-icons">email</span>
                                        <a href="mailto:info@administration.ph">info@administration.ph</a>
                                    </li>
                                </ul>
                            </div>
                            <!-- Footer Contact End -->
                        </div>
                    </div>
                </div>
                <!-- Footer Body End -->

                <!-- Copyright Footer Start -->
                <div class="footer-copyright">
                    <div class="row align-items-center">
                        <div class="col-lg-12">
                            <!-- Footer Copyright Content Start -->
                            <div class="footer-copyright-text">
                                <p>&copy; 2024 Administration.ph. All Rights Reserved.</p>
                            </div>
                            <!-- Footer Copyright Content End -->
                        </div>
                    </div>
                </div>
                <!-- Copyright Footer End -->
            </div>
        </div>
    </div>
</footer>
<!-- Footer End -->
"""

def get_path_prefix(file_path):
    depth = file_path.count(os.sep)
    return '../' * depth

def replace_footer_in_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Regex pattern to match the existing footer
    pattern = re.compile(r'<!-- Footer Start -->.*?<!-- Footer End -->', re.DOTALL)

    path_prefix = get_path_prefix(file_path)
    new_footer = footer_template.format(path_prefix=path_prefix)

    # Replace the existing footer with the new footer
    new_content = re.sub(pattern, new_footer, content)

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(new_content)

def replace_footers_in_project(project_dir):
    for root, dirs, files in os.walk(project_dir):
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                replace_footer_in_file(file_path)

if __name__ == "__main__":
    project_directory = '../'  # Replace with your project directory if not running from project root
    replace_footers_in_project(project_directory)
