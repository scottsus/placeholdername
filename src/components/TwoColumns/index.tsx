import clsx from 'clsx';
import styles from './styles.module.css';

type Props = {
  children: React.ReactNode;
};

export default function TwoColumns({ children }: Props) {
  return <div className={clsx(styles.twoColumns)}>{children}</div>;
}
