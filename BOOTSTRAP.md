# Make Your AI Better at Helping You

This repository helps your AI learn **how you like to work** and turn that into reusable skills.

You do not need to know how skills work.
You do not need to know how to code.
You do not need to choose from hundreds of files.

You can start with one simple request.

## Start here

Give your AI this repository and tell it:

> Read `BOOTSTRAP.md` and help me figure out which skills would make you better at helping me. Look at the work, history, memory, files, tools, and instructions you can actually access. Find things I do again and again. Find skills in this repository that already help with those things. Improve or combine them when that makes sense. Create a new skill only when something useful is truly missing. Do not guess about information you cannot see.

That is the whole starting process.

## What is a skill?

A skill is a reusable set of instructions that teaches an AI how to do something the way you need it done.

For example, maybe you always want your AI to:

- check its work before saying a task is finished
- research before making an important recommendation
- review code in the same careful way every time
- ask before making dangerous changes
- create reports in a format you like
- follow the same steps when fixing bugs

You may already be teaching your AI these things over and over without realizing it.

This repository helps turn those repeated instructions into skills.

## What will it do for me?

Your AI will look for patterns in the information it can access.

It will try to find:

- things you do often
- instructions you keep repeating
- mistakes you keep correcting
- jobs that need the same steps every time
- important rules you do not want forgotten
- skills you already have that work well
- places where a better skill could make your AI more dependable

Then it checks the skills already collected in this repository.

It asks:

**Do we already have a good skill for this?**

If yes, use it.

**Is there a good skill that is close, but needs changes?**

If yes, adapt it to your needs.

**Does your current skill work, but another skill has one really useful idea?**

If yes, borrow that useful part without replacing the way you already work.

**Is something truly missing?**

Only then should it create a new skill.

The goal is not to give you hundreds of skills.

The goal is to give you the **smallest set of skills that actually makes your AI better for you**.

## Why is this useful?

Most AI assistants remember things differently.

You might spend weeks teaching one AI how you like to work, then open another AI and have to start over.

Skills help solve that problem.

Instead of important working habits living only inside one AI's memory, they can live in files that other compatible AI systems can read too.

That means the way you taught ChatGPT to work can help inform Claude, a local agent, or another compatible system later.

The AI systems will not become identical. They have different tools and abilities. But your important working rules do not have to disappear every time you change systems.

## Where do the skills come from?

This repository contains several kinds of skills:

- skills created specifically for this repository
- official skills from companies such as Anthropic, Microsoft, AWS, and Vercel
- selected community skills that are useful enough to study, compare, adapt, or use

For example, the repository can include skills from Matt Pocock's skill collection as an attributed community reference source.

We keep information about where outside skills came from and who created them. If we copy or meaningfully change someone else's work, we keep the required credit and license information.

## It does not blindly copy everything

A popular skill is not automatically a good skill for you.

The bootstrap process compares skills instead of blindly installing them.

It may decide to:

- **USE** a skill that already fits
- **IMPROVE** one of your existing skills
- **ADAPT** another skill to fit your needs
- **BORROW** one useful idea from another skill
- **COMBINE** separate skills that work well together
- **CREATE** a new skill when nothing suitable exists
- **SKIP** a skill that adds no real value

Your way of working stays important. Another person's skill should help your process, not quietly replace it.

## What if my AI cannot see my old conversations or memory?

That is okay.

Different AI systems can access different information.

The bootstrap process should use only what the AI can really see.

If it cannot see your old conversations, it should say that.
If it cannot access your files, it should say that.
If it only has a little information, it should make smaller, more careful recommendations.

It must not pretend it knows things about you that it does not know.

## Will it change things automatically?

Not by default.

The first job is to look, compare, and recommend.

It should not send messages, change permissions, delete things, install software, publish work, or make other important outside changes just because it found a useful skill.

Those actions still need the permission required by the system you are using.

## What do I get at the end?

The bootstrap should give you:

1. **What it noticed**
   The repeated ways you already work.

2. **Which skills would help**
   Including skills you already have, skills that should be improved, and skills worth adding.

3. **A portable skill profile**
   A small file describing the important ways your AI should work with you.

4. **A validation plan**
   A way to test whether the new or improved skills actually make the AI better.

The important part is that the result can live outside one AI's private memory.

## For advanced users and agents

The simple explanation ends here. The machinery underneath it is documented in:

- [`skills/skill-bootstrap/SKILL.md`](skills/skill-bootstrap/SKILL.md) — the full bootstrap procedure
- [`docs/portable-skill-profile.md`](docs/portable-skill-profile.md) — the portable profile format
- [`docs/third-party-provenance.md`](docs/third-party-provenance.md) — rules for credit and source tracking
- [`INDEX.md`](INDEX.md) — the full skill catalog
- [`index.json`](index.json) — the machine-readable catalog
- [`skills/skill-eval/SKILL.md`](skills/skill-eval/SKILL.md) — tests whether a skill actually helps
- [`skills/skill-forge/SKILL.md`](skills/skill-forge/SKILL.md) — creates new repository skills
- [`skills/skill-audit/SKILL.md`](skills/skill-audit/SKILL.md) — checks skills for structural and safety problems
- [`skills/skill-sync/SKILL.md`](skills/skill-sync/SKILL.md) — moves supported skills to other agent hosts

The beginner should not need to understand any of those pieces before getting useful results.
