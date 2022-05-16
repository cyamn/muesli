ALTER TABLE tutorials
ADD COLUMN video_call boolean;

INSERT INTO users (
  email,
  first_name,
  last_name,
  password,
  matrikel,
  birth_date,
  birth_place,
  subject,
  second_subject,
  title,
  is_admin,
  is_assistant
) VALUES (
  'test@test.com',
  'test',
  'test',
  -- password: test
  '$argon2id$v=19$m=65536,t=2,p=1$Ac5/rZUiOVYTlsouxYq4sw$ekkpbPk1zhK8cyI+ZISzGKv4/mzp831LaianUK8Q1fc',
  NULL,
  NULL,
  NULL,
  NULL,
  NULL,
  NULL,
  1,
  0
)