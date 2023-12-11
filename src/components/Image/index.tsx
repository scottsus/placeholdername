import clsx from 'clsx';
import styles from './styles.module.css';

type Props = {
  src: string;
  width?: string;
  alt?: string;
};

export default function Image({ src, width = '100%', alt = 'Image' }: Props) {
  return (
    <img className={clsx(styles.image)} src={src} width={width} alt={alt} />
  );
}
