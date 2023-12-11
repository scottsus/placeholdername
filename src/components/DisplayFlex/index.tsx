import clsx from 'clsx';
import styles from './styles.module.css';

type Props = {
  children: React.ReactNode;
};

export default function DisplayFlex({ children }: Props) {
  return <div className={clsx(styles.DisplayFlex)}>{children}</div>;
}
