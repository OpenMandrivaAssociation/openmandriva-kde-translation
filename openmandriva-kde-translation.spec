Summary:	Localization files for %{distribution} KDE strings
Name:		openmandriva-kde-translation
Version:	2013.0
Release:	5
License:	GPL
Group:		System/Base
URL:		%{disturl}
Source0:	%{name}-%{version}.tar.xz
BuildRequires:	gettext
BuildArch:	noarch
%rename		mandriva-kde-translation

%description
This package includes that translations that have been added on
%{distribution} KDE.

%files -f %{name}.lang
%defattr(-,root,root,0755)

#--------------------------------------------------------------------

%prep
%setup -q -n %{name}

%build

%install
mkdir -p %{buildroot}%{_datadir}/locale

#make po_files
for i in ./*.po
do
  langdir="%{buildroot}%{_datadir}/locale/`basename ${i} .po`/LC_MESSAGES/"
  mkdir -p ${langdir}
  msgfmt -o	${langdir}/%{name}.mo ${i}
done

%find_lang %{name}

