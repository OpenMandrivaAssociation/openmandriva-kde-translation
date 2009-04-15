Summary:	Localization files for Mandriva kde strings
Name:		mandriva-kde-translation
Version:	2009.1
Release:	%mkrel 2
# (nl): see http://svn.mandriva.com/cgi-bin/viewvc.cgi/soft/mandriva-kde-translation/
# generated by `make tarball`
Source0:	%name-%version.tar.bz2

License:	GPL
Group:		System/Base
BuildRoot:	%{_tmppath}/%{name}-%{version}-root
BuildRequires:	gettext
BuildArch:	noarch

%description
This package includes that translations that have been added on
Mandriva KDE.

%prep

%setup -q -n %name

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/locale

#make po_files
for i in ./*.po
do
  langdir="$RPM_BUILD_ROOT%{_datadir}/locale/`basename ${i} .po`/LC_MESSAGES/"
  mkdir -p ${langdir}
  msgfmt -o	${langdir}/mandriva-kde-translation.mo ${i}
done

%find_lang %{name} mandriva-kde-translation

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root,0755)
