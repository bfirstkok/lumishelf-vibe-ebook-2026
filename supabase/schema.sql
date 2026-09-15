-- LumiShelf production schema (Supabase)
create extension if not exists pgcrypto;
create table if not exists public.books (
 id uuid primary key, slug text unique not null, title text not null,
 subtitle text not null, description text not null,
 price numeric(10,2) not null check(price>=0), category text not null,
 pages integer not null check(pages>0), cover_url text not null,
 file_path text not null, active boolean not null default true);
create table if not exists public.orders (
 id uuid primary key default gen_random_uuid(), order_number text unique not null,
 book_id uuid not null references public.books(id), customer_name text not null,
 customer_email text not null, total numeric(10,2) not null check(total>=0),
 status text not null default 'PENDING' check(status in('PENDING','PAID')),
 access_token_hash text not null,
 email_status text not null default 'NOT_SENT' check(email_status in('NOT_SENT','SIMULATED','SENT','FAILED')),
 created_at timestamptz not null default now(), paid_at timestamptz);
alter table public.books enable row level security;
alter table public.orders enable row level security;
revoke all on public.orders from anon,authenticated;
grant all on public.books,public.orders to service_role;
grant select on public.books to anon,authenticated;
drop policy if exists books_active_read on public.books;
create policy books_active_read on public.books for select to anon,authenticated using(active=true);
create index if not exists orders_lookup on public.orders(order_number,customer_email);
insert into storage.buckets(id,name,public) values('ebooks','ebooks',false)
 on conflict(id) do update set public=false;
-- No storage.objects SELECT policy: downloads use server-generated signed URLs only.
