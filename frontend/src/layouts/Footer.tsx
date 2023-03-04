import { NavLogo } from "../components/NavLogo";

export const Footer = () => {
  return (
    <footer>
      <NavLogo />
      <span>
        {new Date().getFullYear()} - Created By{" "}
        <a href="https://github.com/geo-tp">Geo</a> - Django AI
      </span>
    </footer>
  );
};
