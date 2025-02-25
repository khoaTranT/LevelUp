CREATE SCHEMA levelup;

CREATE TYPE sex as ENUM ('male', 'female');
CREATE TYPE visibility as ENUM ('private', 'public');

CREATE TABLE levelup.Users (
	-- account/login info
	user_id SERIAL PRIMARY KEY NOT NULL,
	username VARCHAR(64) UNIQUE NOT NULL,
	passwordHash VARCHAR(64) NOT NULL,

	-- preferences
	mass_unit VARCHAR(16) DEFAULT 'kg',
	energy_unit VARCHAR(16) DEFAULT 'kJ',
	visibility visibility DEFAULT 'private',

	-- health data
	height_m FLOAT(53) CHECK (height_m >= 0),
	mass_kg FLOAT(53) CHECK (mass_kg >= 0),
	age_yr FLOAT(53) CHECK (age_yr >= 0),
	sex sex
);

CREATE TABLE levelup.Meals (
	meal_id SERIAL PRIMARY KEY,
	user_id INT REFERENCES levelup.Users(user_id) ON DELETE CASCADE,
	meal_name VARCHAR(255),
	calories INT CHECK (calories >= 0),
	macronutrients JSONB, -- Stores fats, carbs, proteins
	ingredients JSONB -- Stores the weight of each ingredient
);

CREATE TABLE levelup.HealthGoals (
	goal_id SERIAL PRIMARY KEY,
	user_id INT REFERENCES levelup.Users(user_id) ON DELETE CASCADE,
	target_weight DECIMAL(5,2),
	daily_calorie_goal INT CHECK (daily_calorie_goal >= 0),
	daily_steps_goal INT CHECK (daily_steps_goal >= 0),
	created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE levelup.Exercises (
	exercise_id SERIAL PRIMARY KEY,
	user_id INT REFERENCES levelup.Users(user_id) ON DELETE CASCADE,
	exercise_type VARCHAR(100),
	duration_minutes INT CHECK (duration_minutes >= 0),
	calories_burnt INT CHECK (calories_burnt >= 0)
);

CREATE TABLE levelup.Followers (
	follower_id SERIAL PRIMARY KEY,
	user_id INT REFERENCES levelup.Users(user_id) ON DELETE CASCADE, -- This is the 'followers'
	follows_user_id INT REFERENCES levelup.Users(user_id) ON DELETE CASCADE, -- This is the 'following'
	UNIQUE (user_id, follows_user_id) -- Prevents duplicate follow relationships
);