import media
import fresh_tomatoes

def main():
    # instances of movies
    movie_1 = media.Movie(
        "Ant-Man and the Wasp",
        2018,
        "https://t1.gstatic.com/images?q=tbn:ANd9GcQeA9IA-C1GiNpVwEXXm-jcFOFpuYvjd-n30RmAtSs8511N2NMi",  
        "https://www.youtube.com/watch?v=UUkn-enk2RU"
    )
    movie_2 = media.Movie(
        "Uncle Drew",
        2018,
        "https://t0.gstatic.com/images?q=tbn:ANd9GcQBZ4aPnXEPGrk2HFJ3k9rhO1MlpmuXoCkVvy467ieUM_kIhW42",  
        "https://www.youtube.com/watch?time_continue=1&v=9H2SSvQ8ihA"
    )
    movie_3 = media.Movie(
        "Sanju",
        2018,
        "https://t2.gstatic.com/images?q=tbn:ANd9GcSXZqN6IpcaGlj81n0pybq5mEjPymDiULSoJxJLTOR-qSqdvQr1",  
        "https://www.youtube.com/watch?v=rRr1qiJRsXk"
    )
    movie_4 = media.Movie(
        "Sicario: Day of the Soldado",
        2018,
        "https://t3.gstatic.com/images?q=tbn:ANd9GcTlRDIWlP9HQg5Kkx9naqer1j8snQAGsgsemcEEsUD5l_kTcLGX",  
        "https://www.youtube.com/watch?v=sIMChzE_aCo"
    )
    movie_5 = media.Movie(
        "TAG",
        2018,
        "https://t2.gstatic.com/images?q=tbn:ANd9GcRUSp4bREnGFM6aE037o_VWQ6-UoE5N8OMDQP7jX2ieLT8f2IBG",  
        "https://www.youtube.com/watch?time_continue=2&v=kjC1zmZo30U"
    )
    movie_6 = media.Movie(
        "SuperFly",
        2018,
        "https://t0.gstatic.com/images?q=tbn:ANd9GcQ27l0ix9LU1pHwk3VwIUICAQK6Tdm1d306HmYikxuDAQJLq13M",  
        "https://www.youtube.com/watch?v=aNvRdg1lR7c&t=3s"
    ) 

    # a list contains all the movies
    movies = [
        movie_1, movie_2, movie_3,
        movie_4, movie_5, movie_6,
    ]

    # pass the list the fresh_tomatoes
    fresh_tomatoes.open_movies_page(movies)

if __name__ == '__main__':
    main()