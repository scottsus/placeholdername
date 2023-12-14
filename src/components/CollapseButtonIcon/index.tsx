import clsx from 'clsx';
import styles from './styles.module.css';

type Props = {
  isReversed?: boolean;
};

export default function CollapseButtonIcon({ isReversed = false }: Props) {
  const aboveStyles = [styles.collapseButtonIconBar, styles.above];
  if (isReversed) {
    aboveStyles.push(styles.reversed);
  }

  const belowStyles = [styles.collapseButtonIconBar, styles.below];
  if (isReversed) {
    belowStyles.push(styles.reversed);
  }

  return (
    <div className={clsx(styles.collapseButtonIcon)}>
      <div className={clsx(styles.collapseButtonIconContainer)}>
        <div className={clsx(aboveStyles)}></div>
        <div className={clsx(belowStyles)}></div>
      </div>
      <div className={clsx(styles.tooltip)}>
        {isReversed ? (
          <p
            className={clsx(styles.tooltipText)}
            style={{ transform: 'translateX(100%)' }}
          >
            Open sidebar
          </p>
        ) : (
          <p className={clsx(styles.tooltipText)}>Close sidebar</p>
        )}
        <p className={clsx(styles.tooltipText)}>⌘+\</p>
      </div>
    </div>
  );
}
