Title: GuruPlug heat issues
Date: 2012-11-23 10:20
Category: Linux

My GuruPlug has arrived! Yay!
Soon I'll be replacing my NSLU2 with it, but some clouds are shadowing the horizon.
I didn't have the time to set it up.
Debian 5.03 (lenny) is pre-installed, but only on the device's flash, whose 512MB will probably not suffice to all I want it to do.

<code>
Leporello:~$ ssh root@192.168.1.1
root@192.168.1.1's password: 
Linux sheevaplug-debian 2.6.32-00007-g56678ec #1 PREEMPT Mon Feb 8 03:49:55 PST 2010 armv5tel

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Fri Jan  1 09:19:04 2010 from 192.168.0.2
sheevaplug-debian:~# uname -a
Linux sheevaplug-debian 2.6.32-00007-g56678ec #1 PREEMPT Mon Feb 8 03:49:55 PST 2010 armv5tel GNU/Linux
sheevaplug-debian:~# cat /etc/debian_version 
5.0.3
</code>

Sad thing is, I don't have the time to make all the decisions I need, like "do I need to update U-BOOT?" or "Better to install from scratch or take the
already working Debian installation on my Slug?", like [Martin Michlmayr](http://www.cyrius.com/debian/nslu2/sheevaplug-migration.html) suggests?

On top of that, many users are reporting heat issues, with their GuruPlug Plus even stopping to work with gigabit ethernet plugged in (the photos are very impressive).

http://plugcomputer.org/plugforum/index.php?topic=1735.60

http://www.sheevaplug.de/forum/35-hardware/1744-thermische-probleme.html

New IT is [suggesting](http://www.newit.co.uk/forum/index.php/topic,419.0.html) that people stick to 100MB ethernet (wish would mean that I'm on the clear side with
my non-Gb GuruPlug Standard), but it is [not a safe solution](http://www.newit.co.uk/forum/index.php/topic,423.0.html).

Problems in the components and the montage seem to be the cause as the pictures [here](http://guruplug.daloo.de) document.
Anyway, my first test will simply be to turn it on for a couple of days.
If it's safe, I'll proceed... otherwise have to choose between sending it back to NewIT, selling it, or hacking it.
