"""
This is a simple example of a fasthtml app.
"""
# pylint: disable=unused-wildcard-import, wildcard-import
from fasthtml.common import *

# pylint: disable = undefined-variable

# pylint: disable = function-redefined
css = Style('static/style.css')
app,rt = fast_app(
    pico= False,
    hdrs = (
        Link(rel='stylesheet', href='static/style.css', type='text/css'),
        Link(rel='stylesheet', href='static/tailwind.min.css', type='text/css'),
    )
)

@app.get("/")
def create_main_page():
    """
    Create the main page with translucent background sections.
    Returns:
        A Div component representing the main page.
    """
    return Body(
        create_head_section(),
        create_flex_card_section(),
        create_cards_section(),
        create_nav_section(),
        create_footer_section(),
        cls='antialiased text-black-500 dark:text-slate-400 bg-white dark:bg-slate-900'
    )


def nav_container(children=Any):
    """
    create Navigation container component

    Returns:
        a Nav Ul list of navigation items component.
    """
    return Nav(
        Ul(
            *children,
            cls='flex space-x-3'
        ),
        cls='py-4 px-6 text-sm font-medium'
    )

def nav_item(is_active=False,children=Any,href=None):
    """
    create Navigation Item component

    Returns:
        a Li A link component.
    """
    active = "bg-blue-500 text-white"
    inactive = "bg-slate-50 hover:bg-blue-500 hover:text-white"
    return Li(A(
        children,
        href=href,
        cls='block px-3 py-2 rounded-md '
        f'{ active if is_active else inactive }'
    ))

def movie_list_container(children=Any):
    """
    create a list container component
    Returns:
        Ul(unordered list) component
    """
    return Ul(*children,cls='divide-y divide-slate-100 w-full')

def movie_item_component(movie=Any):
    """
    create a list item component card
    Returns:
        an Article component
    """
    return Article(
        Img(
            src='assets/images/animals.jpg',
            cls= 'w-36 md:40 lg:w-60 h-40 md:64 lg:h-88 flex-none rounded-md bg-slate-100'
        ),
        Div(
            P(
                f"{movie['title']}",
                cls='font-semibold truncate pr-20'
            ),
            Dl(
                Div(
                    Dt(
                        Span(
                            'Star rating',
                            cls='sr-only'
                        ),
                        cls='text-sky-500'
                    ),
                    Dd(
                        f"{movie['star_rating']}",
                        cls=' font-bold'
                    ),
                    cls='absolute top-0 right-0 flex items-center space-x-1'
                ),
                Div(
                    Dt('Rating',cls='sr-only'),
                    Dd(
                        f'{movie["rating"]}',
                        cls='px-1.5 ring-1 ring-slate-200 rounded'
                    )
                ),
                Div(
                    Dt('Year',cls='sr-only'),
                    Dd(
                        f'{movie["year"]}',
                    ),
                    cls='ml-2'
                ),
                Div(
                    Dt('Genre',cls='sr-only'),
                    Dd(
                        f". {movie['genre']}",
                        cls='flex items-center pl-2'
                    ),
                ),
                Div(
                    Dt('duration',cls='sr-only'),
                    Dd(
                        f". {movie['duration']}",
                        cls='flex items-center pl-2'
                    ),
                ),
                Div(
                    Dt('Cast',cls='sr-only'),
                    Dd(
                        ', '.join(movie['cast']),
                        cls='text-slate-400'
                    ),
                    cls='flex-none w-full mt-2 font-normal'
                ),
                cls='mt-2 flex flex-wrap text-sm leading-6 font-medium'
            ),
            cls='min-w-0 relative flex-auto'
        ),
        cls='flex items-start space-x-6 p-6'
    )



def flex_card_container():
    """
    create Navigation container component

    Returns:
        a Nav Ul list of navigation items component.
    """
    return Div(
        Div(
            Img(
                src='assets/images/clothing 2.jpg',
                cls='absolute inset-0 w-full h-full object-cover rounded-l-xl'
            ),
            cls='flex-none w-36 relative'
        ),
        Form(
            Div(
                H1(
                    'Cool Jacket',
                    cls='flex-auto text-lg font-semibold text-slate-900 truncate pr-20'
                ),
                Div("$100",cls='text-lg font-semibold text-slate-500'),
                Div("In stock",
                    cls='w-full flex-none text-sm font-medium text-slate-700 mt-2'
                ),
                cls='flex flex-wrap'
            ),
            Div(
                Div(
                    Label(
                        Input(
                            name='size', type_='radio',value_='xs',
                            cls='sr-only peer'
                        ),
                        Div(
                            "XS",
                            cls='w-9 h-9 rounded-lg flex items-center justify-center '
                            'text-slate-700 peer-checked:font-semibold '
                            'peer-checked:bg-slate-900 peer-checked:text-white'
                        ),
                    ),
                    Label(
                        Input(
                            name='size', type_='radio',value_='s',
                            cls='sr-only peer'
                        ),
                        Div(
                            "S",
                            cls='w-9 h-9 rounded-lg flex items-center justify-center '
                            'text-slate-700 peer-checked:font-semibold '
                            'peer-checked:bg-slate-900 peer-checked:text-white'
                        ),
                    ),
                    Label(
                        Input(
                            name='size', type_='radio',value_='m',
                            cls='sr-only peer'
                        ),
                        Div(
                            "M",
                            cls='w-9 h-9 rounded-lg flex items-center justify-center '
                            'text-slate-700 peer-checked:font-semibold peer-checked:bg-slate-900'
                            ' peer-checked:text-white'
                        ),
                    ),
                    Label(
                        Input(
                            name='size', type_='radio',value_='l',
                            cls='sr-only peer'
                        ),
                        Div(
                            "L",
                            cls='w-9 h-9 rounded-lg flex items-center justify-center '
                            'text-slate-700 peer-checked:font-semibold peer-checked:bg-slate-900'
                            ' peer-checked:text-white'
                        ),
                    ),
                    Label(
                        Input(
                            name='size', type_='radio',value_='xl',
                            cls='sr-only peer'
                        ),
                        Div(
                            "XL",
                            cls='w-9 h-9 rounded-lg flex items-center justify-center '
                            'text-slate-700 peer-checked:font-semibold peer-checked:bg-slate-900'
                            ' peer-checked:text-white'
                        ),
                    ),
                    cls='space-x-2 flex flex-wrap text-sm'
                ),
                cls='flex items-baseline mt-4 mb-6 pb-6 border-b border-slate-200'
            ),
            Div(
                Div(
                    Button("Buy Now",
                        type_='submit',
                        cls='h-10 px-6 font-semibold rounded-md bg-black text-white'
                    ),
                    Button("Add to bag",
                        type_='button',
                        cls='h-10 px-6 font-semibold rounded-md '
                        'border border-slate-200 text-slate-900'
                    ),
                    cls='flex-auto flex flex-wrap space-x-4'
                ),
                Button( "Like",type_='button',
                    cls='flex-none flex items-center justify-center w-9 h-9'
                    ' rounded-md text-slate-300 border border-slate-200'
                ),
                cls='flex flex-wrap space-x-4 mb-6 text-sm font-medium'
            ),
            P("Free shipping on all continental US orders.",
                cls='text-sm text-slate-700'
            ),
            cls='flex-auto p-6'
        ),
        cls='flex font-sans border-b rounded-xl bg-white w-full lg:w-1/2'
    )

def create_head_section():
    """
    Create the about section with a title and paragraph.

    Returns:
        A Div component with an about title and paragraph.
    """
    return Div(
        H1("Become a Fullstack Developer with only Python and FastHTML",
            cls="text-slate-900 font-extrabold "
            "text-4xl sm:text-5xl lg:text-6xl "
            "tracking-tight text-center",
        ),
        P("It contains a description of the website. "
            "The content is divided into sections, with a white background, "
            "a responsive Flex cards, Movie list section ,and a Tile cards section. "
            "This examples demonstrate the use of FastHTML for creating structured "
            "web pages using Python and CSS/Tailwind.",
            cls="mt-6 text-lg text-slate-600 text-center max-w-3xl mx-auto",
        ),
        cls="relative max-w-5xl mx-auto pt-20 sm:pt-24 lg:pt-32"
    )

def create_flex_card_section():
    """
    Create the flex card section.

    Returns:
        A Div component with flex card component.
    """
    return Div(
        H1('Flex Card',cls='pb-10 text-2xl font-semibold'),
        Div(
            flex_card_container(),flex_card_container(),
            cls='flex flex-col lg:flex-row justify-center items-center'
            ' rounded-md p-10 gap-10 bg-black'
        ),
        cls='py-10 px-5 items-center w-full'
    )

def create_nav_section():
    """
    Create the Navigation section.

    Returns:
        A Div component containing tiles.
    """
    nav_list = ['New Releases','Top Rated','Peaks']
    movies = [
        {
            "title": "Prognosis Negative",
            "rating": "PG-13",
            "year": 2021,
            "genre": "Comedy",
            "duration": "1h 46m",
            "cast": ["Simon Pegg", "Zach Galifianakis"],
            "star_rating": 2.66
        },
        {
            "title": "Rochelle, Rochelle",
            "rating": "R",
            "year": 2020,
            "genre": "Romance",
            "duration": "1h 56m",
            "cast": ["Emilia Clarke"],
            "star_rating": 3.25
        },
        {
            "title": "Death Blow",
            "rating": "18A",
            "year": 2020,
            "genre": "Action",
            "duration": "2h 5m",
            "cast": ["Idris Elba", "John Cena", "Thandiwe Newton"],
            "star_rating": 4.95
        }
    ]
    return Div(
        H1('Movie List ',cls='p-10 text-2xl font-semibold'),
        Div(
            Div(
                nav_container(
                    children=[
                        nav_item(
                            children=nav_list[0],href='/new',is_active=True,
                        ),
                        nav_item(
                            children=nav_list[1],href='/top',
                        ),
                        nav_item(
                            children=nav_list[2],href='/picks',
                        )
                    ]
                ),
                movie_list_container(
                    children=[movie_item_component(movie=movie) for movie in movies]
                ),
                cls="flex flex-col w-full lg:w-3/4 border-black bg-black text-white "
                "border-b rounded-xl p-4 pb-6 sm:p-5 sm:pb-4 lg:p-6 items-center"
                "xl:p-10 xl:pb-8 space-y-6 sm:space-y-8 lg:space-y-6 "
                "xl:space-y-8 divide-y divide-slate-100"
            ),
            cls='flex flex-col justify-center items-center w-full'
        ),
        cls='pb-10'
    )

def create_cards_section():
    """
    Create the cards section with responsive tiles.

    Returns:
        A Div component containing tiles.
    """
    images_list = [Img(src=
        "assets/images/photographer.jpg",
        cls="w-6 h-6 rounded-full bg-slate-100 ring-2 ring-white"
        ) for _ in range(5)]
    tiles = [A(
        Dl(
            Div(
                Dt("Title",
                    Dd("Title of card",
                        cls="group-hover:text-white font-semibold text-slate-900"
                    ),
                    cls="sr-only"
                ),
            ),
            Div(
                Dt("Category",
                    Dd("Python Development",
                        cls="group-hover:text-blue-200"
                    ),
                    cls="sr-only"
                ),
            ),
            Div(
                Dt("Users",
                    Dd(*images_list,
                        cls="flex justify-end sm:justify-start"
                        " lg:justify-end xl:justify-start -space-x-1.5"
                    ),
                    cls="sr-only"
                ),
                cls="col-start-2 row-start-1 row-end-3 sm:mt-4 lg:mt-0 xl:mt-4"
            ),
            cls="grid sm:block lg:grid xl:block grid-cols-2 grid-rows-2 items-center"),
        cls= "hover:bg-blue-500 hover:ring-blue-500"
        " hover:shadow-md group rounded-md p-3 bg-white "
        "ring-1 ring-slate-200 shadow-sm"
    ) for _ in range(6)]
    return Div(
        H1('Tiled Cards',cls='p-10 text-2xl font-semibold'),
        Ul(*tiles,
                cls="w-full bg-slate-50 p-4 sm:px-8 sm:pt-6 sm:pb-8"
                " lg:p-4 xl:px-8 xl:pt-6 xl:pb-8 grid grid-cols-1 "
                "sm:grid-cols-2 lg:grid-cols-1 xl:grid-cols-3 gap-4"
                " text-sm leading-6"
    ))

def create_footer_section():
    """
    Create the footer section with copyright and contact links.

    Returns:
        A Div component with footer content.
    """
    return Div(
        P("© 2024 Your Website. All rights reserved.", cls="footer"),
        P("Contact: contact@yourwebsite.com", cls="footer"),
        cls='w-full footer'
    )

serve()
if __name__ == '__main__':
    uvicorn.run("main:app",reload=False)
