Summary:	Localization files for Mandriva KDE strings
Name:		mandriva-kde-translation
Version:	2012.1
Release:	1
License:	GPL
Group:		System/Base
URL:		http://www.rosalinux.com
Source0:	%{name}-%{version}.tar.bz2
BuildRequires:	gettext
BuildArch:	noarch

%description
This package includes that translations that have been added on
Mandriva KDE.

%files -f %{name}.lang
%defattr(-,root,root,0755)

#--------------------------------------------------------------------

%prep
%setup -q -n %{name}

%build

%install
%__mkdir_p %{buildroot}%{_datadir}/locale

#make po_files
for i in ./*.po
do
  langdir="%{buildroot}%{_datadir}/locale/`basename ${i} .po`/LC_MESSAGES/"
  %__mkdir_p ${langdir}
  msgfmt -o	${langdir}/mandriva-kde-translation.mo ${i}
done

%find_lang %{name}

