from project.movie_specification.movie import Movie
from project.user import User


class MovieApp:
    def __init__(self):
        self.movies_collection = []
        self.users_collection = []

    def check_if_user_exists(self, username):
        for user in self.users_collection:
            if user.username == username:
                return True
        return False

    def check_if_movie_exists(self, title):
        for movie in self.movies_collection:
            if movie.title == title:
                return True
        return False

    def check_if_user_liked_movie(self, username, movie_title):
        for user in self.users_collection:
            if user.username == username:
                for movie in user.movies_liked:
                    if movie.title == movie_title:
                        return True
                return False

    def register_user(self, username: str, age: int):
        if self.check_if_user_exists(username):
            raise Exception('User already exists!')

        self.users_collection.append(User(username, age))

        return f"{username} registered successfully."

    def upload_movie(self, username: str, movie: Movie):
        if not self.check_if_user_exists(username):
            raise Exception('This user does not exist!')
        elif self.check_if_movie_exists(movie.title):
            raise Exception('Movie already added to the collection!')
        elif not username == movie.owner.username:
            raise Exception(f'{username} is not the owner of the movie {movie.title}!')
        else:
            self.movies_collection.append(movie)
            for user in self.users_collection:
                if user.username == username:
                    user.movies_owned.append(movie)
                    return f'{username} successfully added {movie.title} movie.'

    def edit_movie(self, username: str, movie: Movie, **kwargs):
        if not self.check_if_movie_exists(movie.title):
            raise Exception(f"The movie {movie.title} is not uploaded!")
        elif not username == movie.owner.username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")
        else:
            for attr, value in kwargs.items():
                setattr(movie, attr, value)

            return f"{username} successfully edited {movie.title} movie."

    def delete_movie(self, username: str, movie: Movie):
        if not self.check_if_movie_exists(movie.title):
            raise Exception(f"The movie {movie.title} is not uploaded!")
        elif not username == movie.owner.username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        self.movies_collection.pop(self.movies_collection.index(movie))
        for user in self.users_collection:
            if user.username == username:
                user.movies_owned.pop(user.movies_owned.index(movie))
                return f"{username} successfully deleted {movie.title} movie."

    def like_movie(self, username: str, movie: Movie):
        if username == movie.owner.username:
            raise Exception(f"{username} is the owner of the movie {movie.title}!")
        elif self.check_if_user_liked_movie(username, movie.title):
            raise Exception(f'{username} already liked the movie {movie.title}!')

        movie.likes += 1
        for user in self.users_collection:
            if user.username == username:
                user.movies_liked.append(movie)

        return f'{username} liked {movie.title} movie.'

    def dislike_movie(self, username: str, movie: Movie):
        if not self.check_if_user_liked_movie(username, movie.title):
            raise Exception(f"{username} has not liked the movie {movie.title}!")

        movie.likes -= 1
        for user in self.users_collection:
            if user.username == username:
                user.movies_liked.pop(user.movies_liked.index(movie))

        return f"{username} disliked {movie.title} movie."

    def display_movies(self):
        if not self.movies_collection:
            return "No movies found."

        result = []
        for movie in sorted(self.movies_collection, key=lambda x: (-x.year, x.title)):
            result.append(movie.details())

        return '\n'.join(result)

    def __str__(self):
        if self.users_collection:
            all_users = f"All users: {', '.join([u.username for u in self.users_collection])}"
        else:
            all_users = "All users: No users."
        if self.movies_collection:
            all_movie = f"All movies: {', '.join([m.title for m in self.movies_collection])}"
        else:
            all_movie = "All movies: No movies."

        result = all_users + "\n" + all_movie

        return result
