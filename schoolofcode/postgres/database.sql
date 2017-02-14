create table public.users (
    id serial primary key,
    email character varying(100),
    firstName character varying(255),
    lastName character varying(255)
)