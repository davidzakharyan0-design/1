import math

movies = [
    {
        "title": "The Dune Chronicles",
        "year": 2021,
        "genres": {"sci-fi", "drama"},
        "rating": 8.6,
        "duration_min": 155,
        "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"],
    },
    {
        "title": "Kitchen Stories",
        "year": 2019,
        "genres": {"comedy", "drama"},
        "rating": 7.1,
        "duration_min": 98,
        "actors": ["A. Novak", "M. Ferguson"],
    },
    {
        "title": "silent hours",
        "year": 2016,
        "genres": {"thriller", "drama"},
        "rating": 6.4,
        "duration_min": 112,
        "actors": ["J. Bloom", "K. Lee"],
    },
    {
        "title": "Comet Racers",
        "year": 2023,
        "genres": {"sci-fi", "action"},
        "rating": 5.9,
        "duration_min": 101,
        "actors": ["O. Isaac", "P. Diaz"],
    },
    {
        "title": "The Last Bakery",
        "year": 2014,
        "genres": {"comedy"},
        "rating": 7.8,
        "duration_min": 89,
        "actors": ["A. Novak", "T. Chalamet"],
    },
    {
        "title": "midnight in oslo",
        "year": 2020,
        "genres": {"thriller", "mystery"},
        "rating": 8.9,
        "duration_min": 124,
        "actors": ["K. Lee", "R. Ferguson"],
    },
    {
        "title": "Garden of Static",
        "year": 2022,
        "genres": {"drama"},
        "rating": 4.8,
        "duration_min": 137,
        "actors": ["P. Diaz", "J. Bloom"],
    },
    {
        "title": "The Quiet Algorithm",
        "year": 2024,
        "genres": {"sci-fi", "drama"},
        "rating": 9.2,
        "duration_min": 118,
        "actors": ["M. Ferguson", "O. Isaac"],
    },
    {
        "title": "Two Left Shoes",
        "year": 2011,
        "genres": {"comedy"},
        "rating": 6.0,
        "duration_min": 95,
        "actors": ["A. Novak", "K. Lee"],
    },
    {
        "title": "Red Harbor",
        "year": 2018,
        "genres": {"action", "thriller"},
        "rating": 7.3,
        "duration_min": 129,
        "actors": ["P. Diaz", "T. Chalamet"],
    },
]


def average_rating(movies):
    if not movies:
        raise ValueError("Каталог пуст: средний рейтинг не определён.")

    total = 0
    for movie in movies:
        total += movie["rating"]

    return round(total / len(movies), 1)


def catalog_age_stats(movies, current_year=2026):
    if not movies:
        raise ValueError("Каталог пуст: возраст фильмов не определён.")

    ages = []
    for movie in movies:
        ages.append(current_year - movie["year"])

    oldest = max(ages)
    newest = min(ages)
    average = math.ceil(sum(ages) / len(ages))

    return oldest, newest, average


def duration_in_hours(minutes):
    hours = minutes // 60
    remaining_minutes = minutes % 60
    return f"{hours}ч {remaining_minutes}м"


def rating_tier(rating):
    if rating >= 9:
        return "шедевр"
    elif rating >= 7:
        return "хорошо"
    else:
        return "средне" if rating >= 5 else "слабо"


def decade_label(year):
    match year:
        case _ if year > 2020:
            return "новые"
        case _ if 2015 <= year <= 2020:
            return "недавние"
        case _:
            return "старые"


def print_non_comedies(movies):
    for movie in movies:
        if "comedy" in movie["genres"]:
            continue
        print(movie["title"])


def print_first_masterpiece(movies):
    index = 0

    while index < len(movies):
        movie = movies[index]
        if movie["rating"] > 9.0:
            print(movie["title"])
            break
        index += 1
    else:
        print("Шедевров не найдено")


def count_long_movies(movies, threshold=120):
    count = 0

    for movie in movies:
        if movie["duration_min"] > threshold:
            count += 1

    return count


def normalize_title(title):
    words = title.split()
    normalized_words = []

    for word in words:
        normalized_words.append(word[0].upper() + word[1:].lower())

    return " ".join(normalized_words)


def make_slug(title):
    return normalize_title(title).lower().replace(" ", "-")


def format_report_line(movie):
    title = normalize_title(movie["title"])
    duration = duration_in_hours(movie["duration_min"])
    genres = ", ".join(sorted(movie["genres"]))

    return (
        f'"{title}" ({movie["year"]}) — '
        f"{movie['rating']:.1f}/10, {duration}, жанры: {genres}"
    )


def titles_sorted_by_rating(movies):
    sorted_movies = sorted(movies, key=lambda movie: movie["rating"], reverse=True)
    return [movie["title"] for movie in sorted_movies]


def top_n_by_rating(movies, n=3):
    if n <= 0:
        return []

    sorted_movies = sorted(movies, key=lambda movie: movie["rating"], reverse=True)

    return [(movie["title"], movie["rating"]) for movie in sorted_movies[:n]]


def count_by_genre(movies):
    counts = {}

    for movie in movies:
        for genre in movie["genres"]:
            counts[genre] = counts.get(genre, 0) + 1

    return counts


def actor_filmography(movies):
    filmography = {}

    for movie in movies:
        for actor in movie["actors"]:
            titles = filmography.get(actor, [])
            titles.append(movie["title"])
            filmography[actor] = titles

    return filmography


def ratings_above_average(movies):
    average = average_rating(movies)

    return {
        movie["title"]: movie["rating"] for movie in movies if movie["rating"] > average
    }


def all_genres(movies):
    genres = set()

    for movie in movies:
        genres.update(movie["genres"])

    return genres


def common_actors(movie1, movie2):
    return set(movie1["actors"]) & set(movie2["actors"])


def genres_only_in_one(movies_a, movies_b):
    return all_genres(movies_a) - all_genres(movies_b)


def iter_high_rated(movies, min_rating=8.0):
    for movie in movies:
        if movie["rating"] >= min_rating:
            yield movie


def print_high_rated(movies):
    for movie in iter_high_rated(movies):
        print(format_report_line(movie))


def total_duration_above_seven(movies):
    return sum(movie["duration_min"] for movie in movies if movie["rating"] > 7)


def build_report(movies):
    print("ОТЧЁТ ПО КАТАЛОГУ")

    if not movies:
        print("Каталог пуст.")
        return

    oldest, newest, average_age = catalog_age_stats(movies)

    print(f"Всего фильмов: {len(movies)}")
    print(f"Средний рейтинг: {average_rating(movies)}")
    print(f"Средний возраст фильмов: {average_age} лет")
    print(f"Возраст самого старого фильма: {oldest} лет")
    print(f"Возраст самого нового фильма: {newest} лет")
    print(f"Фильмов длиннее 120 минут: {count_long_movies(movies)}")

    print("\nТоп-3 фильма:")
    # В исходном каталоге названия уникальны.
    movies_by_title = {movie["title"]: movie for movie in movies}
    for title, _rating in top_n_by_rating(movies):
        print(f"  {format_report_line(movies_by_title[title])}")

    print("\nФильмов по жанрам:")
    genre_counts = count_by_genre(movies)
    sorted_counts = sorted(
        genre_counts.items(),
        key=lambda item: (-item[1], item[0]),
    )
    for genre, count in sorted_counts:
        print(f"  {genre} — {count}")

    print(f"\nВсе жанры каталога: {', '.join(sorted(all_genres(movies)))}")

    print("\nКатегории фильмов и слаги:")
    for movie in movies:
        title = normalize_title(movie["title"])
        tier = rating_tier(movie["rating"])
        period = decade_label(movie["year"])
        slug = make_slug(movie["title"])
        print(f"  {title}: {tier}, {period}, {slug}")

    print("\nФильмы без жанра comedy:")
    print_non_comedies(movies)

    print("\nПервый фильм с рейтингом выше 9:")
    print_first_masterpiece(movies)

    print("\nПроверка поиска в подборке без рейтингов выше 9:")
    without_masterpieces = [movie for movie in movies if movie["rating"] <= 9.0]
    print_first_masterpiece(without_masterpieces)

    print("\nНазвания по убыванию рейтинга:")
    for title in titles_sorted_by_rating(movies):
        print(f"  {normalize_title(title)}")

    print("\nФильмография актёров:")
    filmography = actor_filmography(movies)
    for actor, titles in sorted(filmography.items()):
        formatted_titles = ", ".join(normalize_title(title) for title in titles)
        print(f"  {actor}: {formatted_titles}")

    print("\nФильмы с рейтингом выше среднего:")
    for title, rating in ratings_above_average(movies).items():
        print(f"  {normalize_title(title)}: {rating}")

    if len(movies) >= 4:
        actors = common_actors(movies[0], movies[3])
        actor_names = ", ".join(sorted(actors)) if actors else "нет"
        print("\nОбщие актёры первого и четвёртого фильмов:")
        print(f"  {actor_names}")

    if len(movies) >= 6:
        unique_genres = genres_only_in_one(movies[5:6], movies[:5])
        genre_names = ", ".join(sorted(unique_genres)) or "нет"
        print("\nЖанры шестого фильма, отсутствующие в первых пяти:")
        print(f"  {genre_names}")

    print("\nФильмы с рейтингом не ниже 8:")
    print_high_rated(movies)

    total_minutes = total_duration_above_seven(movies)
    print(f"\nОбщая длительность фильмов с рейтингом выше 7: {total_minutes} мин")


if __name__ == "__main__":
    build_report(movies)
