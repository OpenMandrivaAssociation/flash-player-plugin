%if %mdvver > 3000000
%bcond_with kde
%else
%bcond_without kde
%define x86_64 x86_64
%endif

Summary:	Flash Player plugin for browsers
Name:		flash-player-plugin
Version:	 32.0.0.142
# just update the version, run update.sh and commit
Release:	1
License:	Proprietary
URL:		http://www.adobe.com/products/flashplayer/
Source100:	%{name}.rpmlintrc
Group:		Networking/WWW
ExclusiveArch:	%{ix86} %{x86_64}
Requires(pre):	curl

# helper for getting requires:
# for i in $(objdump -p libflashplayer.so  | grep NEEDED | awk '{ print $2 }' | grep -v ld-linux); do echo "Requires: $i%{_arch_tag_suffix}"; done
Requires:	libatk-1.0.so.0%{_arch_tag_suffix}
Requires:	libcairo.so.2%{_arch_tag_suffix}
Requires:	libc.so.6%{_arch_tag_suffix}
Requires:	libdl.so.2%{_arch_tag_suffix}
Requires:	libfontconfig.so.1%{_arch_tag_suffix}
Requires:	libfreetype.so.6%{_arch_tag_suffix}
Requires:	libgdk_pixbuf-2.0.so.0%{_arch_tag_suffix}
Requires:	libgdk-x11-2.0.so.0%{_arch_tag_suffix}
Requires:	libglib-2.0.so.0%{_arch_tag_suffix}
Requires:	libgmodule-2.0.so.0%{_arch_tag_suffix}
Requires:	libgobject-2.0.so.0%{_arch_tag_suffix}
Requires:	libgthread-2.0.so.0%{_arch_tag_suffix}
Requires:	libgtk-x11-2.0.so.0%{_arch_tag_suffix}
Requires:	libm.so.6%{_arch_tag_suffix}
Requires:	libnspr4.so%{_arch_tag_suffix}
Requires:	libnss3.so%{_arch_tag_suffix}
Requires:	libnssutil3.so%{_arch_tag_suffix}
Requires:	libpango-1.0.so.0%{_arch_tag_suffix}
Requires:	libpangocairo-1.0.so.0%{_arch_tag_suffix}
Requires:	libpangoft2-1.0.so.0%{_arch_tag_suffix}
Requires:	libplc4.so%{_arch_tag_suffix}
Requires:	libplds4.so%{_arch_tag_suffix}
Requires:	libpthread.so.0%{_arch_tag_suffix}
Requires:	librt.so.1%{_arch_tag_suffix}
Requires:	libsmime3.so%{_arch_tag_suffix}
Requires:	libssl3.so%{_arch_tag_suffix}
Requires:	libX11.so.6%{_arch_tag_suffix}
Requires:	libXcursor.so.1%{_arch_tag_suffix}
Requires:	libXext.so.6%{_arch_tag_suffix}
Requires:	libXrender.so.1%{_arch_tag_suffix}
Requires:	libXt.so.6%{_arch_tag_suffix}
# end of helper produced requires

# required for audio, dlopened:
Requires:	libasound.so.2%{_arch_tag_suffix}
# dlopened:
Requires:	libcurl.so.4%{_arch_tag_suffix}
# dlopened, for video acceleration:
Suggests:	libvdpau.so.1%{_arch_tag_suffix}
#
Conflicts:	FlashPlayer < 9.0.115.0-5
Conflicts:	flash-plugin
Conflicts:	FlashPlayer-plugin
Conflicts:	flashplayer-plugin
# Conflict with free plugins to avoid user confusion as to which one is
# actually used:
Conflicts:	gnash-firefox-plugin
Conflicts:	swfdec-mozilla
Conflicts:	lightspark-mozilla-plugin
Conflicts:	libflashsupport < 0.20080000.1
Obsoletes:	flash-player-plugin10.2 < 10.2.152
Provides:	flash-player-plugin11 = %{version}
Obsoletes:	flash-player-plugin11 < %{version}

%description
Adobe Flash Player plugin for browsers.

NOTE: This package does not contain the Flash Player itself. The
software will be automatically downloaded from Adobe during package
installation.

Installing this package indicates acceptance of the Flash Player EULA,
available at http://www.adobe.com/products/eulas/players/flash/
%ifnarch %{x86_64}
and as %{_libdir}/mozilla/plugins/LICENSE.flashplayer.
%endif

%if %{with kde}
# It would be preferable to have the KCM module in the main package with
# simply not requiring any kde stuff. However, standard KDE installation
# doesn't necessary include libkutils4. - Anssi 08/2011
%package kde
Summary:	Flash Player KDE settings module
Group:		Networking/WWW
BuildRequires:	kde4-macros
Requires:	%{name} = %{version}-%{release}
Requires(post):	%{name} = %{version}-%{release}
# helper for getting requires:
# for i in $(objdump -p kcm_adobe_flash_player.so  | grep NEEDED | awk '{ print $2 }' | grep -v ld-linux); do echo "Requires: $i%{_arch_tag_suffix}"; done
Requires:	libc.so.6%{_arch_tag_suffix}
Requires:	libICE.so.6%{_arch_tag_suffix}
Requires:	libkdecore.so.5%{_arch_tag_suffix}
Requires:	libkdeui.so.5%{_arch_tag_suffix}
Requires:	libkutils.so.4%{_arch_tag_suffix}
Requires:	libm.so.6%{_arch_tag_suffix}
Requires:	libpthread.so.0%{_arch_tag_suffix}
Requires:	libQtCore.so.4%{_arch_tag_suffix}
Requires:	libQtDBus.so.4%{_arch_tag_suffix}
Requires:	libQtGui.so.4%{_arch_tag_suffix}
Requires:	libQtSvg.so.4%{_arch_tag_suffix}
Requires:	libSM.so.6%{_arch_tag_suffix}
Requires:	libX11.so.6%{_arch_tag_suffix}
Requires:	libXau.so.6%{_arch_tag_suffix}
Requires:	libXdmcp.so.6%{_arch_tag_suffix}
Requires:	libXext.so.6%{_arch_tag_suffix}
Requires:	libXft.so.2%{_arch_tag_suffix}
Requires:	libXpm.so.4%{_arch_tag_suffix}
# end of helper produced requires
Conflicts:	flash-player-plugin < 10.3.183.5
Provides:	flash-player-plugin11-kde
Obsoletes:	flash-player-plugin11-kde < %{version}

%description kde
KDE settings module for Adobe Flash Player.

NOTE: This package does not contain the software itself. The
software will be automatically downloaded from the Adobe server
during package installation.

Installing this package indicates acceptance of the Flash Player EULA,
available at http://www.adobe.com/products/eulas/players/flash/
%ifnarch %{x86_64}
and as %{_libdir}/mozilla/plugins/LICENSE.flashplayer.
%endif
%endif

%prep
%setup -c -T

# Always prefer versioned archives instead of unversioned ones, so that when
# Adobe updates the Flash Player, the old sha256sum continues to work until
# this package is updated for the new version.

# The linuxdownload.adobe.com rpm usually stays up longer, but fpdownload.macromedia.com is faster.
# Their sha256sums usually differ.

%ifarch %ix86
%define downurl1	http://fpdownload.macromedia.com/get/flashplayer/pdc/%{version}/flash-player-npapi-%{version}-release.i386.rpm
# (Anssi) this was up faster (i.e. at the time of writing it was up but downurl1 was not), but does not stay up very long, same sha256 as url1:
%define downurl2	http://fpdownload.macromedia.com/get/flashplayer/current/licensing/linux/flash-player-npapi-%{version}-release.i386.rpm
# can be temporarily disabled by %nilling if not yet available at the time of updating:
%define downurl3	http://linuxdownload.adobe.com/linux/i386/flash-player-npapi-%{version}-release.i386.rpm
%define downurl4	%nil

# sha256sum:filesize
%define tsha256sum1	bbb12724cf3f27ef793044cf5853e66ea3e7bfebbabed77553b20070fadf39b9:8505827
%define tsha256sum2	:
%define tsha256sum3	67e572c8ad84a035d71bd8257346e468e915afaadba2db159542b8ed49d12a34:8506083

%define tarname		flash-player-npapi-%{version}-release.i386.rpm

%define warn_on_missing_files 1
%endif

%ifarch %{x86_64}
%define downurl1	http://fpdownload.macromedia.com/get/flashplayer/pdc/%{version}/flash-player-npapi-%{version}-release.x86_64.rpm
%define downurl2	http://fpdownload.macromedia.com/get/flashplayer/current/licensing/linux/flash-player-npapi-%{version}-release.x86_64.rpm
%define downurl3	http://linuxdownload.adobe.com/linux/x86_64/flash-player-npapi-%{version}-release.x86_64.rpm
%define downurl4	%nil

%define tsha256sum1	9a757f3b5acfd8155e59085a5d2376339bfc1a71b63cdfc3985af9686a98f3fb:9022392
%define tsha256sum2	:
%define tsha256sum3	9b14f95beae159baba3a8d38f8f94691ef8270ebd0760b88bbe2d21b08683d79:9022568

%define tarname		flash-player-npapi-%{version}-release.x86_64.rpm

%define warn_on_missing_files 1
%endif

%define file %{_localstatedir}/lib/%{name}/%{tarname}

%install

install -d -m755 %{buildroot}%{_localstatedir}/lib/%{name}
install -d -m755 %{buildroot}%{_libdir}/mozilla/plugins
touch %{buildroot}%{_libdir}/mozilla/plugins/libflashplayer.so
touch %{buildroot}%{_libdir}/mozilla/plugins/LICENSE.flashplayer
touch %{buildroot}%{_libdir}/mozilla/plugins/README.flashplayer
touch %{buildroot}%{_localstatedir}/lib/%{name}/%{tarname}

install -d -m755 %{buildroot}%{_bindir}
touch %{buildroot}%{_bindir}/flash-player-properties

%if %{with kde}
install -d -m755 %{buildroot}%{_kde_services}
touch %{buildroot}%{_kde_services}/kcm_adobe_flash_player.desktop
install -d -m755 %{buildroot}%{_kde_libdir}/kde4
touch %{buildroot}%{_kde_libdir}/kde4/kcm_adobe_flash_player.so
%endif

install -d -m755 %{buildroot}%{_datadir}/applications
touch %{buildroot}%{_datadir}/applications/flash-player-properties.desktop

for i in 16 22 24 32 48; do
	install -d -m755 %{buildroot}%{_iconsdir}/hicolor/${i}x${i}/apps
	touch %{buildroot}%{_iconsdir}/hicolor/${i}x${i}/apps/flash-player-properties.png
done

install -d -m755 %{buildroot}%{_datadir}/%{name}
cat > %{buildroot}%{_datadir}/%{name}/functions << EOF
next_file() {
	FILENUM=\$((FILENUM+1))
	eval FILE_SRC="\\\$FILE\${FILENUM}_SRC"
	eval FILE_DST="\\\$FILE\${FILENUM}_DST"
	eval FILE_PRM="\\\$FILE\${FILENUM}_PRM"
	[ -n "\$FILE_SRC" ]
}

tar_extract() {
        extractdir=\$(mktemp -d --tmpdir=/tmp)
	if [ -z "\$extractdir" ]; then
		echo "Error during extraction." >&2
		exit 1
	fi

	cd "\$extractdir" || exit 1

	if [ "\$(head -c4 "%file")" = \$'\\xED\\xAB\\xEE\\xDB' ]; then
		rpm2cpio "%file" | cpio -i --quiet -d -R root:root
	else
		tar -xzf "%file" --no-same-owner --no-same-permissions
	fi

	# Avoid leaving old files in case of failure below
	FILENUM=0
	while next_file; do
		rm -f "\$FILE_DST"
	done

	FILENUM=0
	while next_file; do
		if [ ! -f "\$FILE_SRC" ]; then
%if %warn_on_missing_files
			echo "Warning: \$FILE_SRC not found in the Flash Player archive," >&2
			echo "         skipping installation of \$FILE_DST." >&2
			echo "         Please file a bug report at https://openmandriva.org/ ." >&2
%endif
			continue
		fi
		chmod "\$FILE_PRM" "\$FILE_SRC"
		mv -f "\$FILE_SRC" "\$FILE_DST"
	done
	rm -rf "\$extractdir"
}
EOF

%pre
checksha256sum() {
	[ -e "$1" ] || return 1
	FILESHA256="$(sha256sum $1 | cut -d" " -f1)"
	FILESIZE="$(stat -c%%s "$1")"
	[ -n "$FILESHA256" ] || return 1
	[ -n "$FILESIZE" ] || return 1
	SHA256NUM=1
	eval SHA256SUM="\$SHA256SUM$SHA256NUM"
	while [ "$SHA256SUM" ]; do
		[ "${SHA256SUM%:*}" = "$FILESHA256" ] && [ "${SHA256SUM#*:}" = "$FILESIZE" ] && return 0
		SHA256NUM=$((SHA256NUM+1))
		eval SHA256SUM="\$SHA256SUM$SHA256NUM"
	done
	return 1
}

get_proxy_from_urpmi() {
	if [ -e /etc/urpmi/proxy.cfg ]; then
		proxy="$(grep ^http_proxy= /etc/urpmi/proxy.cfg 2>/dev/null)"
		proxy_user="$(grep ^proxy_user= /etc/urpmi/proxy.cfg 2>/dev/null)"

		proxy="${proxy#http_proxy=}"
		proxy_user="${proxy_user#proxy_user=}"

		[ -n "$proxy" ] && echo "--proxy $proxy"
		[ -n "$proxy_user" ] && echo "--proxy-user $proxy_user"
	fi
}

SHA256SUM1="%{tsha256sum1}"
SHA256SUM2="%{tsha256sum2}"
SHA256SUM3="%{tsha256sum3}"
SHA256SUM4=
URL1="%{downurl1}"
URL2="%{downurl2}"
URL3="%{downurl3}"
URL4=

URLNUM=1

install -d -m 0755 %{_localstatedir}/lib/%{name}

echo "Note that by downloading the Adobe Flash Player you indicate your acceptance of"
echo "the EULA, available at http://www.adobe.com/products/eulas/players/flash/"
while ! checksha256sum "%file"; do
	eval URL="\$URL$URLNUM"
	if [ -z "$URL" ]; then
		echo "Error: Unable to download Flash Player. This is likely due to this package" >&2
		echo "       being too old. Please file a bug report at %{bugurl}" >&2
		echo "       so that the package gets updated. Thank you." >&2
		echo "" >&2
		echo "       In the meantime, you can download Flash Player manually from" >&2
		echo "       http://get.adobe.com/flashplayer/" >&2
		rm -f "%file"
		[ "$(ls -A "%{_localstatedir}/lib/%{name}")" ] && rm -rf "%{_localstatedir}/lib/%{name}"
		exit 1
	fi
	URLNUM=$((URLNUM+1))
	echo "Downloading from $URL:"
	curl --connect-timeout 20 -m 10800 -L $(get_proxy_from_urpmi) "$URL" > "%file"
done

%post
FILE1_SRC="usr/%{_lib}/flash-plugin/libflashplayer.so"
FILE1_DST="%{_libdir}/mozilla/plugins/libflashplayer.so"
FILE1_PRM="0755"
FILE2_SRC="usr/share/doc/flash-plugin-%{version}/license.pdf"
FILE2_DST="%{_libdir}/mozilla/plugins/LICENSE.flashplayer"
FILE2_PRM="0644"
FILE3_SRC="usr/share/doc/flash-plugin-%{version}/readme.txt"
FILE3_DST="%{_libdir}/mozilla/plugins/README.flashplayer"
FILE3_PRM="0644"

FILE4_SRC="usr/bin/flash-player-properties"
FILE4_DST="%{_bindir}/flash-player-properties"
FILE4_PRM="0755"
FILE5_SRC="usr/share/applications/flash-player-properties.desktop"
FILE5_DST="%{_datadir}/applications/flash-player-properties.desktop"
FILE5_PRM="0644"

FILE6_SRC="usr/share/icons/hicolor/16x16/apps/flash-player-properties.png"
FILE6_DST="%{_iconsdir}/hicolor/16x16/apps/flash-player-properties.png"
FILE6_PRM="0644"
FILE7_SRC="usr/share/icons/hicolor/22x22/apps/flash-player-properties.png"
FILE7_DST="%{_iconsdir}/hicolor/22x22/apps/flash-player-properties.png"
FILE7_PRM="0644"
FILE8_SRC="usr/share/icons/hicolor/24x24/apps/flash-player-properties.png"
FILE8_DST="%{_iconsdir}/hicolor/24x24/apps/flash-player-properties.png"
FILE8_PRM="0644"
FILE9_SRC="usr/share/icons/hicolor/32x32/apps/flash-player-properties.png"
FILE9_DST="%{_iconsdir}/hicolor/32x32/apps/flash-player-properties.png"
FILE9_PRM="0644"
FILE10_SRC="usr/share/icons/hicolor/48x48/apps/flash-player-properties.png"
FILE10_DST="%{_iconsdir}/hicolor/48x48/apps/flash-player-properties.png"
FILE10_PRM="0644"
FILE11_SRC=

. %{_datadir}/%{name}/functions
tar_extract

# show in KDE as well (in case user doesn't have -kde subpkg
sed -i 's,NotShowIn=KDE;,,' %{_datadir}/applications/flash-player-properties.desktop 2>/dev/null || :
# otherwise KDE hides it:
sed -i 's,GNOME;,,' %{_datadir}/applications/flash-player-properties.desktop 2>/dev/null || :

echo "Adobe Flash Player installation successful."

%if %{with kde}
%pre kde
# When installing both main package and -kde, failure of %pre of main package
# can prevent installation of it, but urpmi/rpm will try to install -kde
# regardless. FIXME.
# For now, workaround it by preventing -kde installation as well:
[ -e %{_datadir}/%{name}/functions ] && [ -e %{_localstatedir}/lib/%{name}/%{tarname} ]

%post kde
FILE1_SRC="usr/%{_lib}/kde4/kcm_adobe_flash_player.so"
FILE1_DST="%{_kde_libdir}/kde4/kcm_adobe_flash_player.so"
FILE1_PRM="0755"
FILE2_SRC="usr/share/kde4/services/kcm_adobe_flash_player.desktop"
FILE2_DST="%{_kde_services}/kcm_adobe_flash_player.desktop"
FILE2_PRM="0644"
FILE3_SRC=

. %{_datadir}/%{name}/functions
tar_extract

sed -i 's,=personal,=network-and-connectivity,' %{_kde_services}/kcm_adobe_flash_player.desktop 2>/dev/null || :

%endif

%files
%dir %{_localstatedir}/lib/%{name}
%ghost %{_localstatedir}/lib/%{name}/%{tarname}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/functions

%dir %{_libdir}/mozilla
%dir %{_libdir}/mozilla/plugins
%ghost %{_libdir}/mozilla/plugins/libflashplayer.so
%ghost %{_libdir}/mozilla/plugins/LICENSE.flashplayer
%ghost %{_libdir}/mozilla/plugins/README.flashplayer

%ghost %{_bindir}/flash-player-properties
%ghost %{_datadir}/applications/flash-player-properties.desktop
%ghost %{_iconsdir}/hicolor/*/apps/flash-player-properties.png

%if %{with kde}
%files kde
%ghost %{_kde_libdir}/kde4/kcm_adobe_flash_player.so
%ghost %{_kde_services}/kcm_adobe_flash_player.desktop
%endif

