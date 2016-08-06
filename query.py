"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise directions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()

# -------------------------------------------------------------------
# Part 2: Write queries


# Get the brand with the **id** of 8.

Brand.query.get(8)

# Get all models with the **name** Corvette and the **brand_name** Chevrolet.

Model.query.filter_by(name="Corvette", brand_name="Chevrolet").all()

# Get all models that are older than 1960.

Model.query.filter(Model.year < 1960).all()

# Get all brands that were founded after 1920.

Brand.query.filter(Brand.founded > 1920).all()

# Get all models with names that begin with "Cor".

Model.query.filter(Model.name.like('Cor%')).all()

# Get all brands that were founded in 1903 and that are not yet discontinued.

Brand.query.filter(Brand.founded==1903, Brand.discontinued==None).all()

# Get all brands that are either 1) discontinued (at any time) or 2) founded 
# before 1950.

Brand.query.filter((Brand.discontinued != None) | (Brand.founded < 1950)).all()

# Get any model whose brand_name is not Chevrolet.

Model.query.filter(Model.brand_name != "Chevrolet").all()

# Fill in the following functions. (See directions for more info.)

def get_model_info(year):
    '''Takes in a year, and prints out each model, brand_name, and brand
    headquarters for that year using only ONE database query.'''

    models = Model.query.filter(Model.year==year).all()

    for model in models:
        print model.name, model.brand_name, model.brand.headquarters

def get_brands_summary():
    '''Prints out each brand name, and each model name for that brand
     using only ONE database query.'''

    brands = Model.query.all()

    brands_models = []

    for brand in brands:
        brands_models.append((brand.brand_name, brand.name))

    summary_list = list(set(brands_models))

    return summary_list




# -------------------------------------------------------------------
# Part 2.5: Discussion Questions (Include your answers as comments.)

# 1. What is the returned value and datatype of ``Brand.query.filter_by(name='Ford')``?
"""This query returns a Brand object that contains the attributes that are associated with 
the brand name Ford."""
# 2. In your own words, what is an association table, and what *type* of relationship
# does an association table manage?
"""An association table is a table that connects two tables with one another. 
The table doesn't contain any fields with any additional information. It 
serves solely as a link."""
# -------------------------------------------------------------------
# Part 3

def search_brands_by_name(mystr):
    query = Brand.query.filter(Brand.name.like('%mystr%')).all()
    return query    


def get_models_between(start_year, end_year):
    brands = Brand.query.filter((Brand.founded > start_year) & (Brand.discontinued < end_year)).all()
    models = []
    for brand in brands:
        models.append(brand.model.name)
    return models

















