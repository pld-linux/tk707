Summary:	Drum sequencer for a sound card or MIDI device
#Summary(pl.UTF-8):	-
Name:		tk707
Version:	0.8
Release:	2
License:	GPL v2
Group:		Applications/Multimedia
Source0:	http://www-ljk.imag.fr/membres/Pierre.Saramito/tk707/download/%{name}-%{version}.tar.gz
# Source0-md5:	7471494195c053f048862c292320d06c
Source1:	%{name}.desktop
Patch0:		%{name}-build.patch
URL:		http://www-ljk.imag.fr/membres/Pierre.Saramito/tk707/
BuildRequires:	alsa-lib-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	flex
BuildRequires:	tcl-devel
BuildRequires:	texi2html
BuildRequires:	texinfo-texi2dvi
BuildRequires:	texlive-format-pdflatex
BuildRequires:	tk-devel
BuildRequires:	transfig
BuildRequires:	xorg-lib-libICE-devel
BuildRequires:	xorg-lib-libX11-devel
Suggests:	TiMidity++
Suggests:	TiMidity++-alsaseq
Suggests:	lame
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This program emulates the operation of Roland's TR-707 Rhythm
Composer.

The output is to a MIDI device, sound card or file.
A Latin-percussion instrument map emulates the Roland TR-727 and
the instrument map can be customized by the user. If you do not
have a MIDI sound card, you should install the timidity package
to emulate one.

#%description -l pl.UTF-8

%prep
%setup -q
%{__sed} -i -e 's|\\$|"|g' -e 's|^|"|g' defs.c
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}

%configure \
	LAME=/usr/bin/lame \
	TIMIDITY=/usr/bin/timidity \
	MIDIDUMP=/usr/bin/mididump

%{__make}
%{__make} tk707.pdf

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/html

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog INSTALL NEWS README TODO tk707.html tk707.pdf
%attr(755,root,root) %{_bindir}/tk707
%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/tk707bin
%{_datadir}/%{name}
%{_infodir}/tk707.info*
%{_mandir}/man1/tk707.1*
%{_desktopdir}/%{name}.desktop
