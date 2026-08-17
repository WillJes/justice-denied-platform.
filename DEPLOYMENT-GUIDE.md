# Put Justice Denied on GitHub and Vercel

## 1. Create GitHub repository

1. Sign in at github.com and select **New repository**.
2. Name it `justice-denied-platform`.
3. Choose **Private** while preparing it.
4. Do not add a README, .gitignore, or license; they are included.
5. Create the repository.

## 2. Upload the site

1. Unzip the downloaded package.
2. Open the empty repository and select **Add file → Upload files**.
3. Drag in the contents of the unzipped folder—not the outer folder.
4. Use the message `First Justice Denied website` and commit.

If browser upload skips folders, use GitHub Desktop: **File → Add Local Repository**, select the unzipped folder, then publish it privately.

## 3. Deploy on Vercel

1. Sign in at vercel.com with GitHub.
2. Select **Add New → Project**.
3. Import `justice-denied-platform`.
4. Vercel should detect **Next.js** automatically.
5. Leave root directory, build command, and output directory on their defaults.
6. Select **Deploy**, then open the address Vercel provides.

## 4. Add a domain later

Open the Vercel project, go to **Settings → Domains**, add your domain, and follow the DNS directions.

## 5. Future updates

Edit `app/page.tsx` in GitHub and commit. Vercel automatically deploys the update.

## Before launch

- Add the real donation link and speaker photo.
- Confirm festival names and statuses.
- Test the booking email.
- Redact archive records.
- Add captions or transcripts for videos.
- Connect your chosen domain.
