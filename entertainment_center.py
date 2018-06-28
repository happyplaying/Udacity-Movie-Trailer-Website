import media
import fresh_tomatoes

def main():
    # instances of movies
    movie_1 = media.Movie(
        "n9ukI7khQpE",
        "Adrift",
        "Tami Oldham and Richard Sharp couldn't anticipate that they would be sailing directly into one of the most catastrophic hurricanes in recorded history. In the aftermath of the storm, Tami awakens to find Richard badly injured and their boat in ruins. With no hope of rescue, Tami must now find the strength and determination to save herself and the only man she has ever loved.",
        2018,
        "https://t0.gstatic.com/images?q=tbn:ANd9GcT4AgGfM-EHToOFIbMBFo0Of8U9YCCfHhaCkiG2S55TwSaNUaT8",  
        "https://www.youtube.com/watch?v=n9ukI7khQpE"
    )
    movie_2 = media.Movie(
        "9H2SSvQ8ihA",
        "Uncle Drew",
        "After draining his life savings to enter a team in the Rucker Classic street ball tournament in Harlem, Dax (Lil Rel Howery) is dealt a series of unfortunate setbacks, including losing his team to his longtime rival (Nick Kroll).",
        2018,
        "https://t0.gstatic.com/images?q=tbn:ANd9GcQBZ4aPnXEPGrk2HFJ3k9rhO1MlpmuXoCkVvy467ieUM_kIhW42",  
        "https://www.youtube.com/watch?time_continue=1&v=9H2SSvQ8ihA"
    )
    movie_3 = media.Movie(
        "rRr1qiJRsXk",
        "Sanju",
        "Coming from a family of cinematic legends, East Indian actor Sanjay Dutt reaches dizzying heights of success -- but also battles numerous addictions and other personal demons.",
        2018,
        "https://t2.gstatic.com/images?q=tbn:ANd9GcSXZqN6IpcaGlj81n0pybq5mEjPymDiULSoJxJLTOR-qSqdvQr1",  
        "https://www.youtube.com/watch?v=rRr1qiJRsXk"
    )
    movie_4 = media.Movie(
        "20bpjtCbCz0",
        "Deadpool 2",
        "Wisecracking mercenary Deadpool meets Russell, an angry teenage mutant who lives at an orphanage. When Russell becomes the target of Cable -- a genetically enhanced soldier from the future -- Deadpool realizes that he'll need some help saving the boy from such a superior enemy. He soon joins forces with Bedlam, Shatterstar, Domino and other powerful mutants to protect young Russell from Cable and his advanced weaponry.",
        2018,
        "https://t2.gstatic.com/images?q=tbn:ANd9GcTkbXNbwGV0npOKCGSndE-YCGpRb2xQDRV8VyMfGlsEfej-sVMv",  
        "https://www.youtube.com/watch?v=20bpjtCbCz0"
    )
    movie_5 = media.Movie(
        "43MBOJnVks",
        "Rampage",
        "Global icon Dwayne Johnson headlines the action adventure Rampage, directed by Brad Peyton. Johnson stars as primatologist Davis Okoye, a man who keeps people at a distance but shares an unshakable bond with George, the extraordinarily intelligent, incredibly rare albino silverback gorilla who has been in his care since he rescued the young orphan from poachers. But a rogue genetic experiment gone awry mutates this gentle ape into a raging creature of enormous size. ",
        2018,
        "https://t1.gstatic.com/images?q=tbn:ANd9GcQpTCKCvU_Fz0SwP_oyuSSKdf_unn88WWa5evQC4F3U7EfHyQVJ",  
        "https://www.youtube.com/watch?v=-43MBOJnVks"
    )
    movie_6 = media.Movie(
        "aNvRdg1lR7c",
        "SuperFly",
        "Cocaine kingpin Youngblood Priest realizes that it's time to get out of the game after surviving a violent attack from a crazed rival. Hoping for one last score, Priest and his partner travel to Mexico to arrange a deal. The career criminal now finds himself trying to outmaneuver the cartel, two corrupt police officers and all the double-crossers that threaten his path to freedom.",
        2018,
        "https://t0.gstatic.com/images?q=tbn:ANd9GcQ27l0ix9LU1pHwk3VwIUICAQK6Tdm1d306HmYikxuDAQJLq13M",  
        "https://www.youtube.com/watch?v=aNvRdg1lR7c&t=3s"
    ) 
    movie_7 = media.Movie(
        "ri1Cc3Yz09U",
        "Action Point",
        "D.C. is the crackpot owner of Action Point -- a low-rent, out-of-control amusement park where the rides are designed with minimum safety for maximum fun. Just as his estranged daughter Boogie comes to visit, a corporate mega-park opens nearby and jeopardizes the future of Action Point. To save his beloved park and his relationship with Boogie, D.C. and his loony crew of misfits must risk everything to pull out all the stops and save the day.",
        2018,
        "https://t1.gstatic.com/images?q=tbn:ANd9GcQ4l1S6iJ_Q1mKmgZABtJfPvuIYBxVZzfBSbGqazUKFW5WxKk-K",  
        "https://www.youtube.com/watch?v=ri1Cc3Yz09U"
    ) 
    movie_8 = media.Movie(
        "JqfuKsoEEms",
        "Hotel Artemis",
        "As rioting rocks Los Angeles in the year 2028, disgruntled thieves make their way to Hotel Artemis -- a 13-story, members-only hospital for criminals. It's operated by the Nurse, a no-nonsense, high-tech healer who already has her hands full with a French assassin, an arms dealer and an injured cop. As the violence of the night continues, the Nurse must decide whether to break her own rules and confront what she's worked so hard to avoid.",
        2018,
        "https://t0.gstatic.com/images?q=tbn:ANd9GcQcV4REDtRQfcPRgpaEliePGpuYDZ1dUmzpr6o3DutzUv2FJ2TE",  
        "https://www.youtube.com/watch?time_continue=1&v=JqfuKsoEEms"
    ) 


    # a list contains all the movies
    movies = [
        movie_1, movie_2, movie_3,
        movie_4, movie_5, movie_6,
        movie_7,movie_8
    ]

    # pass the list the fresh_tomatoes
    fresh_tomatoes.open_movies_page(movies)

if __name__ == '__main__':
    main()