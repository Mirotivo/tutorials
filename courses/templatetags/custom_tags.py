from django import template
from datetime import datetime

register = template.Library()

# @register.inclusion_tag('footer.html')
# def show_footer():
#     current_year = datetime.now().year
#     return {'year': current_year}
